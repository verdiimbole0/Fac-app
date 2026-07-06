require("dotenv").config();
const express = require("express");
const cors = require("cors");

const authRoutes = require("./routes/auth");
const paymentRoutes = require("./routes/payments");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/health", (_req, res) => res.json({ status: "ok", app: "Fac'App API" }));

app.use("/api/auth", authRoutes);
app.use("/api/payments", paymentRoutes);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Fac'App API démarrée sur le port ${PORT}`);
});
