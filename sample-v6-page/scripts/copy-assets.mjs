import { cp, mkdir } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(process.cwd());
const src = resolve(root, "node_modules/govuk-frontend/dist/govuk/assets");
const dest = resolve(root, "dist/assets");

await mkdir(dest, { recursive: true });
await cp(src, dest, { recursive: true });

const jsSrc = resolve(root, "node_modules/govuk-frontend/dist/govuk/govuk-frontend.min.js");
const jsDest = resolve(root, "dist/govuk-frontend.min.js");
await cp(jsSrc, jsDest);

console.log("Copied govuk-frontend assets + JS to dist/");
