FROM node:20-bookworm

# Set the working directory
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package files and install dependencies
COPY package*.json ./
RUN pnpm install

# Copy start.sh and make it executable (as root)
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

# Copy the rest of your application code
COPY . .

# Switch to the non-root user
USER node

EXPOSE 3000

# Start the application
CMD ["bash", "./start.sh"]