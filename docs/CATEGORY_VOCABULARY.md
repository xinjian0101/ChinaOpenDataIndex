# Category Vocabulary

A controlled category vocabulary improves search, review, and downstream export.

## Initial categories

| Identifier | English label | Chinese label | Scope |
|---|---|---|---|
| `economy` | Economy | 经济 | macroeconomics, industry, trade, business indicators |
| `education` | Education | 教育 | schools, enrollment, examinations, learning resources |
| `environment` | Environment | 环境 | air, water, emissions, weather observations, ecology |
| `health` | Health | 健康 | public-health statistics and service metadata |
| `population` | Population | 人口 | census, demographic, household, migration statistics |
| `public-services` | Public Services | 公共服务 | administrative and community services |
| `science` | Science and Technology | 科技 | research, patents, innovation, laboratories |
| `transport` | Transport | 交通 | roads, transit, traffic, logistics, mobility |
| `urban` | Urban Development | 城市建设 | planning, housing, infrastructure, land use |
| `other` | Other | 其他 | records that cannot yet be classified reliably |

## Assignment rules

- Select one primary category based on the publisher's stated subject.
- Use tags for secondary topics.
- Do not create a new category for one record.
- Use `other` temporarily when evidence is insufficient.
- Record proposed vocabulary changes in a reviewed commit.

## Versioning

The vocabulary should gain a version identifier before automated validation depends on it. Renaming or merging identifiers requires migration notes because stored records may reference the previous values.

## Bilingual consistency

English and Chinese labels are display values. The identifier is the stable machine-readable value. Translations should be reviewed for domain meaning rather than translated word by word.
