// Entry for make.fun news-image-20261123 (Node 22, standard library only):
// the image is the entry.png beside this file, and the program copies it
// to /output/entry.png. Deterministic: byte-for-byte identical every run.
// The output is left world-readable (0644): the grader collects it as
// another user.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync } from 'node:fs';
import { join } from 'node:path';

const out = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), out);
chmodSync(out, 0o644);
