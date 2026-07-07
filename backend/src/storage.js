const path = require("path");
const fs = require("fs");

// Stockage des documents de la messagerie.
// - "local" (défaut) : fichiers dans backend/uploads/ — pour le développement.
// - "s3" : tout service compatible S3 (AWS S3, Supabase Storage, Cloudflare R2...),
//   activé en renseignant STORAGE_DRIVER=s3 et les variables S3_* dans .env.
const DRIVER = process.env.STORAGE_DRIVER || "local";

const UPLOADS_DIR = path.join(__dirname, "..", "uploads");
fs.mkdirSync(UPLOADS_DIR, { recursive: true });

let s3Client = null;
function getS3() {
  if (!s3Client) {
    const { S3Client } = require("@aws-sdk/client-s3");
    s3Client = new S3Client({
      region: process.env.S3_REGION || "auto",
      endpoint: process.env.S3_ENDPOINT || undefined,
      forcePathStyle: process.env.S3_FORCE_PATH_STYLE === "true",
      credentials: {
        accessKeyId: process.env.S3_ACCESS_KEY_ID,
        secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
      },
    });
  }
  return s3Client;
}

// Multer écrit d'abord le fichier dans UPLOADS_DIR (storedName) ; en driver s3
// on le téléverse ensuite dans le bucket puis on supprime la copie locale.
async function saveFile(storedName, mimeType) {
  if (DRIVER === "local") return;

  const { PutObjectCommand } = require("@aws-sdk/client-s3");
  const localPath = path.join(UPLOADS_DIR, storedName);
  await getS3().send(
    new PutObjectCommand({
      Bucket: process.env.S3_BUCKET,
      Key: storedName,
      Body: fs.createReadStream(localPath),
      ContentType: mimeType || "application/octet-stream",
    })
  );
  await fs.promises.unlink(localPath);
}

// Envoie le document au client avec son nom d'origine.
async function sendFile(res, storedName, fileName) {
  if (DRIVER === "local") {
    return res.download(path.join(UPLOADS_DIR, storedName), fileName);
  }

  const { GetObjectCommand } = require("@aws-sdk/client-s3");
  const object = await getS3().send(
    new GetObjectCommand({ Bucket: process.env.S3_BUCKET, Key: storedName })
  );
  res.setHeader("Content-Disposition", `attachment; filename="${encodeURIComponent(fileName)}"`);
  if (object.ContentType) res.setHeader("Content-Type", object.ContentType);
  object.Body.pipe(res);
}

module.exports = { UPLOADS_DIR, saveFile, sendFile };
