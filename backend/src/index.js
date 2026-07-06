require("dotenv").config();
const express = require("express");
const cors = require("cors");

const authRoutes = require("./routes/auth");
const paymentRoutes = require("./routes/payments");
const sessionRoutes = require("./routes/sessions");
const tutorRoutes = require("./routes/tutors");
const messageRoutes = require("./routes/messages");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/health", (_req, res) => res.json({ status: "ok", app: "Fac'App API" }));

app.use("/api/auth", authRoutes);
app.use("/api/payments", paymentRoutes);
app.use("/api/sessions", sessionRoutes);
app.use("/api/sessions", messageRoutes); // fil de discussion et documents d'une session
app.use("/api/tutors", tutorRoutes);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Fac'App API démarrée sur le port ${PORT}`);
});
