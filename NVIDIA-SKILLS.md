# NVIDIA Agent Skills (vendored)

This repository vendors the full catalog of **NVIDIA-verified Agent Skills**
alongside its own marketing/SEO skills. All NVIDIA skills live in `skills/`
next to the existing ones.

## Source

| | |
|---|---|
| Upstream | https://github.com/NVIDIA/skills |
| Commit | `c9e2ce9f76ec1a2a8a5df919bd28b6a8fdf4cf56` |
| Vendored on | 2026-09-14 |
| Skills added | 355 |

`skills/NVIDIA-CATALOG.md` is upstream's catalog index (renamed from
`skills/README.md` so it does not shadow this repo's own skills directory).

## Licensing and attribution

Upstream is dual-licensed: **Apache-2.0** for source code and **CC BY-4.0**
for documentation and skill content. Copies of both live in `licenses/`:

- `licenses/NVIDIA-LICENSE-APACHE`
- `licenses/NVIDIA-LICENSE-CC-BY-4.0`

Skill content is © 2026 NVIDIA Corporation, used under CC BY-4.0. Individual
skills may declare a narrower license in their `SKILL.md` front matter —
that declaration governs the skill it appears in.

## Signature verification

Each NVIDIA skill ships a detached signature at `<skill>/skill.oms.sig`.
The signing root certificate is vendored at `licenses/nv-agent-root-cert.pem`,
and `licenses/nvidia-versions.json` records the upstream `content_digest` and
`last_commit` for every skill, so a vendored copy can be checked against the
version it was taken from.

## Updating

The upstream catalog re-syncs from NVIDIA product repos daily. To refresh:

```bash
git clone --depth 1 https://github.com/NVIDIA/skills.git /tmp/nvidia-skills
cp -r /tmp/nvidia-skills/skills/. skills/
mv skills/README.md skills/NVIDIA-CATALOG.md
cp /tmp/nvidia-skills/versions.json licenses/nvidia-versions.json
cp /tmp/nvidia-skills/nv-agent-root-cert.pem licenses/nv-agent-root-cert.pem
```

Then update the commit SHA and date in the table above.

## Scope note

These skills cover CUDA-X, Physical AI and robotics, simulation, medical
imaging, networking and RAG workflows — a very different domain from this
repo's marketing and SEO skills. They share the `skills/` directory, so an
agent loading this repo sees all 389 skill descriptions at once. If that
becomes noisy, moving the NVIDIA set into its own directory (or installing it
via `npx skills add nvidia/skills` instead of vendoring) is the cleaner fix.
