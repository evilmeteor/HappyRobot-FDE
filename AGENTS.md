# Repository Guidelines

## Project Structure & Module Organization
The repository currently contains only high-level docs; as you add code, keep the root lean. Place runtime modules in `src/` using language-appropriate packaging (`src/happy_robot/` for Python packages or `src/happy_robot` for Rust crates). Keep automated scripts in `tools/` and infra artifacts in `infra/` (Terraform, Ansible, etc.). Put design notes in `docs/` and user-facing assets under `assets/`. Tests should mirror the runtime layout inside `tests/` with the same module names. Use feature branches to prototype larger reorganizations; never commit generated build outputs.

## Build, Test, and Development Commands
Expose all repeatable workflows through a root `Makefile` so collaborators can run one-liners. Examples:
- `make setup` installs or updates dependencies (delegate to `scripts/setup.sh` or the language's package manager).
- `make lint` runs formatters and static analyzers.
- `make test` executes the whole test suite headlessly.
Document extra language-specific commands (e.g., `poetry install`, `npm run dev`) inside the README and ensure they are invoked by the Make targets to keep parity.

## Coding Style & Naming Conventions
Adopt the formatter native to your implementation language (`ruff`/`black` for Python, `prettier` for TypeScript, `rustfmt` for Rust) and run it before every commit. Prefer 2-space indentation for YAML and 4 spaces for code unless the language enforces otherwise. Module names stay lowercase with underscores; classes use PascalCase; constants are UPPER_SNAKE. Keep function names verbs describing behavior (`encrypt_volume`, `sync_robot_state`). Prefer explicit typing where supported.

## Testing Guidelines
Create unit tests under `tests/<module_name>/test_<scenario>.py` (or the language-equivalent). Use high-level acceptance tests in `tests/integration/` to cover disk-encryption flows end-to-end, mocking external robotics services when needed. Target ≥80% coverage and document significant gaps. Run `make test` locally before pushing; when adding encryption or security-critical logic, add regression tests that fail without the new change.

## Commit & Pull Request Guidelines
Follow Conventional Commits (`feat:`, `fix:`, `chore:`) to keep history searchable. Keep commits small, focused, and linted. Pull requests must include a concise summary, linked issue or ticket ID, testing notes (`make test`, `make lint`), and screenshots or logs for UI/security tooling. Request review from at least one maintainer; respond to feedback with follow-up commits rather than force-pushing unless rebasing on main.

## Security & Configuration Tips
Store secrets in environment files tracked by your password manager, never in Git. Validate encryption keys and certificates in CI before deployment. Document any required kernel modules or OS dependencies in `docs/security.md`, and update provisioning scripts whenever configuration steps change.
