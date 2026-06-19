# Source Acceptance Policy

This policy determines whether a catalog record can be added to ChinaOpenDataIndex. It applies to metadata records, not to redistribution of the underlying dataset.

## Accept

A record may be accepted when:

- the publisher can be identified;
- the source page is publicly reachable without account access;
- the dataset title and category can be confirmed;
- the record stores metadata only;
- the declared license or access terms are recorded accurately;
- the Chinese and English names are faithful to the source;
- no personal information is copied into the catalog record;
- verification status and date are included when review has occurred.

## Hold for review

A record should be held when:

- the publisher appears legitimate but the exact source page is unclear;
- the license label conflicts with the visible terms;
- access requires an application or approval;
- the English name is uncertain;
- the page is reachable but the download is unavailable;
- multiple catalog entries may refer to the same dataset;
- commercial reuse conditions are not explicit.

## Reject

A record should be rejected when:

- the source is a user profile, forum post, private share, or login-only page;
- the publisher cannot be identified;
- the record would expose personal information or secret access details;
- the title, publisher, or license is fabricated or inferred without evidence;
- the source explicitly prohibits indexing or the intended metadata use;
- the entry is primarily an advertisement rather than a dataset catalog record;
- the record copies restricted source data instead of metadata.

## Evidence fields

Recommended fields:

```json
{
  "source_url": "https://example.invalid/catalog/001",
  "verification_status": "verified",
  "verified_at": "2026-06-19",
  "evidence_note": "publisher, title, access page, and declared terms reviewed",
  "review_required": false
}
```

## License handling

Use the license field to record what the source declares. Do not convert unclear terms into a standard open license without evidence.

Recommended status values:

- `verified-open`
- `declared-open-unverified`
- `restricted`
- `application-required`
- `terms-unclear`
- `unknown`

## Translation rules

- Preserve the dataset scope.
- Do not translate “available” as “open for commercial use” unless the source states that.
- Keep organization names consistent across records.
- Retain important geographic and temporal qualifiers.
- Record a translation note when the English title is editorial rather than official.

## Re-verification

Recheck a record when:

- the source link fails;
- the publisher changes its catalog platform;
- the license or terms change;
- the download method changes;
- a contributor reports outdated metadata;
- the record has not been reviewed within the project’s chosen interval.

Structural validation is necessary, but evidence review remains a human responsibility.