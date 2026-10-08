# Build Stage
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production Nginx Stage
FROM nginx:alpine

# Copy built assets to Nginx default public directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration if applicable
# COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]