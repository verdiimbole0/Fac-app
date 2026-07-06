FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY prisma ./prisma
RUN npx prisma generate

COPY src ./src

ENV NODE_ENV=production
EXPOSE 4000

# Applique les migrations puis démarre l'API
CMD ["sh", "-c", "npx prisma migrate deploy && node src/index.js"]
