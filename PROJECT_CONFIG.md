# Project Configuration Template

**Purpose:** A neutral template for user-, team-, and project-specific settings. Copy and fill only what is confirmed. Blank or `UNCONFIGURED` values are unknown and must not be treated as defaults or approval.

> This template is intentionally generic. Do not copy configuration from an unrelated user, previous project, sample, or repository without confirming that it applies to the active task.

## 1. Owner and project scope

```yaml
profile_version: 1
owner_or_team: UNCONFIGURED
project_name: UNCONFIGURED
project_type: UNCONFIGURED
project_description: UNCONFIGURED
primary_domain_or_app_id: UNCONFIGURED
repository: UNCONFIGURED
jurisdiction_and_region: UNCONFIGURED
source_of_truth: UNCONFIGURED
approval_authority: UNCONFIGURED
```

## 2. Communication preferences

```yaml
language: MATCH_USER
reading_level: MATCH_USER
technical_depth: MATCH_TASK
tone: DIRECT_AND_RESPECTFUL
format_preferences: []
accessibility_needs: []
preferred_decision_summary:
  - verdict
  - reasons
  - risks
  - better_option
  - next_step
ethical_frameworks_or_user_values: []
```

Only fill `ethical_frameworks_or_user_values` with values the user has explicitly stated or confirmed. These preferences must never override truth, safety, privacy, consent, law, or higher-priority instructions.

## 3. Runtime and hosting environment

```yaml
operating_system: UNCONFIGURED
operating_system_version: VERIFY_LIVE
web_server: UNCONFIGURED
php_or_runtime_version: VERIFY_LIVE
runtime_sapi: VERIFY_LIVE
framework_and_version: UNCONFIGURED
hosting_provider: UNCONFIGURED
hosting_type: UNCONFIGURED
root_or_admin_access: VERIFY
actual_document_root: VERIFY
private_storage_root: VERIFY
memory_limit: VERIFY_LIVE
upload_limit: VERIFY_LIVE
post_limit: VERIFY_LIVE
execution_timeout: VERIFY_LIVE
required_extensions_or_modules: VERIFY_LIVE
services_available: VERIFY_LIVE
services_prohibited: []
```

Do not rely on this section until the live target has been checked. CLI and web runtime settings may differ. Do not assume Redis, root access, a particular PHP extension, or a specific web server exists.

## 4. Application architecture and coding standards

```yaml
architecture_style: UNCONFIGURED
frontend_stack: UNCONFIGURED
backend_stack: UNCONFIGURED
database_engine_and_version: VERIFY_LIVE
css_strategy: UNCONFIGURED
javascript_strategy: UNCONFIGURED
asset_build_pipeline: UNCONFIGURED
shared_component_strategy: REQUIRED_WHERE_REUSED
api_contract_format: UNCONFIGURED
coding_style_guide: UNCONFIGURED
supported_browsers: UNCONFIGURED
supported_devices_and_breakpoints: UNCONFIGURED
accessibility_target: VERIFY_OR_AGREE
```

For websites/web applications, also apply the mandatory unified UI/UX, responsive design, reusable component, frontend/backend separation, and sensitive-file isolation requirements in `SKILL_RULES.md` §1.

## 5. Security and privacy posture

```yaml
secrets_storage_location: OUTSIDE_DOCUMENT_ROOT_WHERE_POSSIBLE
sensitive_data_classes: []
data_retention_policy: UNCONFIGURED
backup_policy: UNCONFIGURED
logging_policy: UNCONFIGURED
authentication_methods: UNCONFIGURED
authorization_model: UNCONFIGURED
mfa_requirement: UNCONFIGURED
csrf_and_session_policy: VERIFY_OR_DEFINE
upload_policy: UNCONFIGURED
privacy_and_consent_requirements: UNCONFIGURED
incident_contact_or_process: UNCONFIGURED
```

Never store real passwords, tokens, private keys, recovery codes, or personal identity data in this template. Store secret values in a secure secrets manager or private server-side configuration, not in a skill file or repository.

## 6. Delivery and approval controls

```yaml
environments: []
staging_available: VERIFY
production_change_approval_required: true
backup_before_change: true
rollback_method: UNCONFIGURED
test_requirements: []
acceptance_criteria: []
release_owner: UNCONFIGURED
external_publication_approval: REQUIRED
```

## 7. Budget and integration limits

```yaml
budget_or_cost_ceiling: UNCONFIGURED
api_cost_constraints: UNCONFIGURED
allowed_external_services: []
prohibited_external_services: []
rate_or_quota_limits: VERIFY_LIVE
required_data_residency: UNCONFIGURED
```

Prefer efficient, maintainable solutions and avoid unnecessary API calls, dependencies, or paid services. Do not reduce quality, security, privacy, or reliability merely to reduce cost.

## 8. Change history

| Date (ISO 8601) | Field changed | Previous value | New value | Confirmed by | Evidence/source |
|---|---|---|---|---|---|
| UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED |

## 9. Configuration acceptance checklist

- [ ] Confirm this profile belongs to the active owner and project.
- [ ] Verify volatile runtime, server, library, API, and provider details live.
- [ ] Confirm the true document root and private storage location.
- [ ] Confirm user preferences and ethical values rather than inferring them.
- [ ] Confirm production, financial, external-publication, and destructive-action approval authority.
- [ ] Remove any secrets or unnecessary personal data before sharing or committing this file.
