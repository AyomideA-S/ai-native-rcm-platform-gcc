#!/bin/bash

# Start Next.js dev server and keep it in the foreground
pnpm run dev

# Run watcher.js (if needed) and wait
if [ -f "./watcher.js" ]; then
  node watcher.js
else
  echo "watcher.js not found, skipping..."
fi

# wait is implicit if pnpm run dev runs indefinitely