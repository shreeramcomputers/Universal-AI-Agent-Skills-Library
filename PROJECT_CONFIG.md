# Project Configuration Template

**Version:** 3.0.0  
**Purpose:** Neutral settings for an individual, team, organization, or project. Copy and fill only what is verified or explicitly approved. Blank, UNCONFIGURED, and VERIFY values are unknown—not defaults, consent, or approval.

Do not copy values from another user, organization, prior project, sample, or repository without confirming applicability. Never store real secrets in this file.

## 1. Identity and scope

```yaml
profile_version: "3.0.0"
owner_or_team: UNCONFIGURED
project_name: UNCONFIGURED
project_type: UNCONFIGURED
project_description: UNCONFIGURED
repository_url: UNCONFIGURED
primary_domain_or_app_id: UNCONFIGURED
jurisdiction_and_region: UNCONFIGURED
source_of_truth: UNCONFIGURED
approval_authority: UNCONFIGURED
```

## 2. Communication and accessibility

```yaml
language: MATCH_USER
reading_level: MATCH_USER
technical_depth: MATCH_TASK
tone: DIRECT_AND_RESPECTFUL
format_preferences: []
accessibility_needs: []
ethical_frameworks_or_user_values: []
```

Only record values the user has explicitly stated or confirmed. These preferences do not override truth, safety, privacy, consent, law, or platform rules.

## 3. Runtime, hosting, and deployment

```yaml
operating_system: UNCONFIGURED
operating_system_version: VERIFY_LIVE
runtime_and_version: VERIFY_LIVE
runtime_sapi_or_execution_mode: VERIFY_LIVE
framework_and_version: VERIFY_LIVE
database_engine_and_version: VERIFY_LIVE
hosting_provider: UNCONFIGURED
hosting_type: UNCONFIGURED
root_or_admin_access: VERIFY
actual_document_root: VERIFY
private_storage_root: VERIFY
memory_and_request_limits: VERIFY_LIVE
upload_and_execution_limits: VERIFY_LIVE
available_extensions_or_modules: VERIFY_LIVE
available_services: VERIFY_LIVE
prohibited_services: []
backup_and_restore_capability: VERIFY
```

Check live web/runtime settings separately from CLI settings. Do not assume root access, Redis, Docker, a specific PHP extension, or any provider feature.

## 4. Architecture and interface standards

```yaml
architecture_style: UNCONFIGURED
frontend_stack: UNCONFIGURED
backend_stack: UNCONFIGURED
database_stack: VERIFY_LIVE
css_strategy: UNCONFIGURED
javascript_strategy: UNCONFIGURED
asset_pipeline: UNCONFIGURED
shared_component_strategy: REUSE_WHERE_APPROPRIATE
api_contract_format: UNCONFIGURED
coding_style: UNCONFIGURED
supported_browsers: UNCONFIGURED
supported_devices_and_breakpoints: UNCONFIGURED
accessibility_target: VERIFY_OR_AGREE
testing_frameworks: UNCONFIGURED
```

For websites and browser tools, use one consistent product-wide design system, reusable header/footer/navigation/components, separate CSS and JavaScript, clear frontend/backend separation, fully responsive layouts, and private-file isolation as specified in SKILL_RULES.md §1.

## 5. Security, privacy, and data governance

```yaml
secrets_storage_location: OUTSIDE_DOCUMENT_ROOT_WHERE_POSSIBLE
authentication_model: UNCONFIGURED
authorization_model: UNCONFIGURED
mfa_requirement: UNCONFIGURED
sensitive_data_classes: []
data_minimization_rules: UNCONFIGURED
retention_and_deletion_policy: UNCONFIGURED
backup_policy: UNCONFIGURED
logging_and_telemetry_policy: UNCONFIGURED
privacy_and_consent_requirements: UNCONFIGURED
incident_response_process: UNCONFIGURED
```

Never put password values, API tokens, private keys, recovery codes, OTPs, payment credentials, or unnecessary identity/customer data here. Store secrets in a proper secrets manager or private server-side configuration.

## 6. Delivery and approval controls

```yaml
environments: []
staging_available: VERIFY
production_change_approval_required: true
external_publication_approval_required: true
backup_before_change: true
rollback_or_recovery_method: UNCONFIGURED
required_test_gates: []
acceptance_criteria: []
release_owner: UNCONFIGURED
```

## 7. Budget and third-party integrations

```yaml
budget_or_cost_ceiling: UNCONFIGURED
api_cost_constraints: UNCONFIGURED
allowed_external_services: []
prohibited_external_services: []
rate_and_quota_limits: VERIFY_LIVE
data_residency_requirements: UNCONFIGURED
vendor_exit_requirements: UNCONFIGURED
```

Prefer efficient, maintainable solutions. Do not reduce security, privacy, quality, or reliability merely to reduce cost.

## 8. Change history

| Date (ISO 8601) | Field changed | Previous value | New value | Confirmed by | Evidence/source |
|---|---|---|---|---|---|
| UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED | UNCONFIGURED |

## 9. Acceptance checklist

- [ ] Confirm this profile belongs to the active user/team and project.
- [ ] Verify volatile runtime, provider, API, software, and policy details live.
- [ ] Confirm actual document root and private storage location.
- [ ] Confirm permissions, approval authority, and deployment access.
- [ ] Confirm user preferences rather than inferring them.
- [ ] Remove secrets and unnecessary personal data before saving or sharing.
