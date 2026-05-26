# Matrix Project - Technical Database Schema Reference

## Quick Reference for Report Generation

---

## DATABASE TABLES SUMMARY

| Table Name            | Django Model | App       | Records Purpose                  | Key Fields                                      |
| --------------------- | ------------ | --------- | -------------------------------- | ----------------------------------------------- |
| accounts_user         | User         | accounts  | User authentication & profiles   | id, username, email, password                   |
| hume_thumb            | thumb        | hume      | Main content thumbnails          | id, title, dinak (date), thumbnail_image        |
| aimlo_thumb_aimlo     | thumb_aimlo  | aimlo     | AI/ML content thumbnails         | id, title, dinak, thumbnail_image               |
| cybero_thumb_cybero   | thumb_cybero | cybero    | Cybersecurity content thumbnails | id, title, dinak, thumbnail_image               |
| webo_thumb_webo       | thumb_webo   | webo      | Web dev content thumbnails       | id, title, dinak, thumbnail_image               |
| videos_video          | Video        | videos    | Main hub videos                  | id, title, video_file, date, text (HTML), image |
| vid_aiml_video_aiml   | Video_aiml   | vid_aiml  | AI/ML videos                     | id, title, video_file, date, text (HTML), image |
| vid_cyber_video_cyber | Video_cyber  | vid_cyber | Cybersecurity videos             | id, title, video_file, date, text (HTML), image |
| vid_web_video_web     | Video_web    | vid_web   | Web development videos           | id, title, video_file, date, text (HTML), image |

---

## DETAILED TABLE SPECIFICATIONS

### 1. accounts_user Table

```
Table: accounts_user
Model: accounts.models.User
Purpose: User account storage and authentication

Columns:
┌─────────────────┬───────────────┬──────────────┬─────────────────────┐
│ Column Name     │ Type          │ Constraints  │ Description         │
├─────────────────┼───────────────┼──────────────┼─────────────────────┤
│ id              │ BigAutoField  │ PK, AUTO    │ Primary Key         │
│ username        │ CharField(150)│ UNIQUE, NN  │ Login username      │
│ email           │ EmailField    │ UNIQUE, NN  │ User email address  │
│ password        │ CharField(225)│ NOT NULL    │ Hashed password     │
└─────────────────┴───────────────┴──────────────┴─────────────────────┘

Constraints:
- UNIQUE on (username)
- UNIQUE on (email)
- No foreign keys

Data Sample:
id=1, username='john_doe', email='john@example.com', password='pbkdf2_sha256$...'
```

### 2. hume_thumb Table

```
Table: hume_thumb
Model: hume.models.thumb
Purpose: Main hub content thumbnails and metadata

Columns:
┌─────────────────┬──────────────────┬──────────────┬─────────────────────┐
│ Column Name     │ Type             │ Constraints  │ Description         │
├─────────────────┼──────────────────┼──────────────┼─────────────────────┤
│ id              │ BigAutoField     │ PK, AUTO    │ Primary Key         │
│ title           │ CharField(60)    │ NOT NULL    │ Content title       │
│ dinak           │ DateField        │ NOT NULL    │ Upload date         │
│ thumbnail_image │ FileField(250)   │ NULL        │ Path to thumbnail   │
└─────────────────┴──────────────────┴──────────────┴─────────────────────┘

File Storage: media/thumbnail/
Sample Path: media/thumbnail/content_01.jpg

Data Sample:
id=1, title='Python Basics', dinak='2024-01-15', thumbnail_image='media/thumbnail/python.jpg'
```

### 3. aimlo_thumb_aimlo Table

```
Table: aimlo_thumb_aimlo
Model: aimlo.models.thumb_aimlo
Purpose: AI/ML category content thumbnails

Columns:
┌─────────────────┬──────────────────┬──────────────┬─────────────────────┐
│ Column Name     │ Type             │ Constraints  │ Description         │
├─────────────────┼──────────────────┼──────────────┼─────────────────────┤
│ id              │ BigAutoField     │ PK, AUTO    │ Primary Key         │
│ title           │ CharField(60)    │ NOT NULL    │ Content title       │
│ dinak           │ DateField        │ NOT NULL    │ Upload date         │
│ thumbnail_image │ FileField(250)   │ NULL        │ Path to thumbnail   │
└─────────────────┴──────────────────┴──────────────┴─────────────────────┘

File Storage: media/thumbnail/
Category: AI/Machine Learning
Related View: /aiml route

Data Sample:
id=1, title='Neural Networks', dinak='2024-02-10', thumbnail_image='media/thumbnail/nn.jpg'
```

### 4. cybero_thumb_cybero Table

```
Table: cybero_thumb_cybero
Model: cybero.models.thumb_cybero
Purpose: Cybersecurity category content thumbnails

Columns:
┌─────────────────┬──────────────────┬──────────────┬─────────────────────┐
│ Column Name     │ Type             │ Constraints  │ Description         │
├─────────────────┼──────────────────┼──────────────┼─────────────────────┤
│ id              │ BigAutoField     │ PK, AUTO    │ Primary Key         │
│ title           │ CharField(60)    │ NOT NULL    │ Content title       │
│ dinak           │ DateField        │ NOT NULL    │ Upload date         │
│ thumbnail_image │ FileField(250)   │ NULL        │ Path to thumbnail   │
└─────────────────┴──────────────────┴──────────────┴─────────────────────┘

File Storage: media/thumbnail/
Category: Cybersecurity
Related View: /cyber route

Data Sample:
id=1, title='Network Security', dinak='2024-01-20', thumbnail_image='media/thumbnail/security.jpg'
```

### 5. webo_thumb_webo Table

```
Table: webo_thumb_webo
Model: webo.models.thumb_webo
Purpose: Web Development category content thumbnails

Columns:
┌─────────────────┬──────────────────┬──────────────┬─────────────────────┐
│ Column Name     │ Type             │ Constraints  │ Description         │
├─────────────────┼──────────────────┼──────────────┼─────────────────────┤
│ id              │ BigAutoField     │ PK, AUTO    │ Primary Key         │
│ title           │ CharField(60)    │ NOT NULL    │ Content title       │
│ dinak           │ DateField        │ NOT NULL    │ Upload date         │
│ thumbnail_image │ FileField(250)   │ NULL        │ Path to thumbnail   │
└─────────────────┴──────────────────┴──────────────┴─────────────────────┘

File Storage: media/thumbnail/
Category: Web Development
Related View: /web route

Data Sample:
id=1, title='HTML & CSS', dinak='2024-02-05', thumbnail_image='media/thumbnail/web.jpg'
```

### 6. videos_video Table

```
Table: videos_video
Model: videos.models.Video
Purpose: Main hub video content storage with rich media support

Columns:
┌─────────────────┬──────────────────────┬──────────────┬──────────────────────┐
│ Column Name     │ Type                 │ Constraints  │ Description          │
├─────────────────┼──────────────────────┼──────────────┼──────────────────────┤
│ id              │ BigAutoField         │ PK, AUTO    │ Primary Key          │
│ title           │ CharField(255)       │ NOT NULL    │ Video title          │
│ video_file      │ FileField            │ NOT NULL    │ Path to video file   │
│ date            │ DateTimeField        │ AUTO_SET    │ Upload timestamp     │
│ text            │ HTMLField (TinyMCE)  │ NOT NULL    │ Rich HTML content    │
│ image           │ ImageField           │ NULL        │ Thumbnail image      │
└─────────────────┴──────────────────────┴──────────────┴──────────────────────┘

File Storage:
- video_file: media/vid/
- image: media/photo/

Related Views:
- /video/<id>/ (display)
- /saveenquiry (create)
- / (homepage display)

Data Sample:
id=1,
title='Introduction to Python',
video_file='media/vid/python_intro.mp4',
date='2024-01-15 10:30:00',
text='<h2>Python Basics</h2><p>Learn python fundamentals...</p>',
image='media/photo/python_thumb.jpg'
```

### 7. vid_aiml_video_aiml Table

```
Table: vid_aiml_video_aiml
Model: vid_aiml.models.Video_aiml
Purpose: AI/ML category video storage

Columns:
┌─────────────────┬──────────────────────┬──────────────┬──────────────────────┐
│ Column Name     │ Type                 │ Constraints  │ Description          │
├─────────────────┼──────────────────────┼──────────────┼──────────────────────┤
│ id              │ BigAutoField         │ PK, AUTO    │ Primary Key          │
│ title           │ CharField(255)       │ NOT NULL    │ Video title          │
│ video_file      │ FileField            │ NOT NULL    │ Path to video file   │
│ date            │ DateTimeField        │ AUTO_SET    │ Upload timestamp     │
│ text            │ HTMLField (TinyMCE)  │ NOT NULL    │ Rich HTML content    │
│ image           │ ImageField           │ NULL        │ Thumbnail image      │
└─────────────────┴──────────────────────┴──────────────┴──────────────────────┘

Category: AI/Machine Learning
Related View: /video_of_aiml/<id>/

File Storage: media/vid/, media/photo/
```

### 8. vid_cyber_video_cyber Table

```
Table: vid_cyber_video_cyber
Model: vid_cyber.models.Video_cyber
Purpose: Cybersecurity category video storage

Columns:
┌─────────────────┬──────────────────────┬──────────────┬──────────────────────┐
│ Column Name     │ Type                 │ Constraints  │ Description          │
├─────────────────┼──────────────────────┼──────────────┼──────────────────────┤
│ id              │ BigAutoField         │ PK, AUTO    │ Primary Key          │
│ title           │ CharField(255)       │ NOT NULL    │ Video title          │
│ video_file      │ FileField            │ NOT NULL    │ Path to video file   │
│ date            │ DateTimeField        │ AUTO_SET    │ Upload timestamp     │
│ text            │ HTMLField (TinyMCE)  │ NOT NULL    │ Rich HTML content    │
│ image           │ ImageField           │ NULL        │ Thumbnail image      │
└─────────────────┴──────────────────────┴──────────────┴──────────────────────┘

Category: Cybersecurity
Related View: /video_of_cyber/<id>/

File Storage: media/vid/, media/photo/
```

### 9. vid_web_video_web Table

```
Table: vid_web_video_web
Model: vid_web.models.Video_web
Purpose: Web Development category video storage

Columns:
┌─────────────────┬──────────────────────┬──────────────┬──────────────────────┐
│ Column Name     │ Type                 │ Constraints  │ Description          │
├─────────────────┼──────────────────────┼──────────────┼──────────────────────┤
│ id              │ BigAutoField         │ PK, AUTO    │ Primary Key          │
│ title           │ CharField(255)       │ NOT NULL    │ Video title          │
│ video_file      │ FileField            │ NOT NULL    │ Path to video file   │
│ date            │ DateTimeField        │ AUTO_SET    │ Upload timestamp     │
│ text            │ HTMLField (TinyMCE)  │ NOT NULL    │ Rich HTML content    │
│ image           │ ImageField           │ NULL        │ Thumbnail image      │
└─────────────────┴──────────────────────┴──────────────┴──────────────────────┘

Category: Web Development
Related View: /video_of_web/<id>/

File Storage: media/vid/, media/photo/
```

---

## DATABASE RELATIONSHIPS

```
Logical Relationships (No Foreign Keys Implemented)

accounts_user ─→ (No direct relationships)
                  └─ Can be enhanced to link with views/likes/comments

hume_thumb ────→ videos_video (1-to-1 logical mapping)
                 └─ Both store content related to same item

aimlo_thumb_aimlo ──→ vid_aiml_video_aiml (1-to-1 logical mapping)
                      └─ Denormalized by category

cybero_thumb_cybero ──→ vid_cyber_video_cyber (1-to-1 logical mapping)
                        └─ Denormalized by category

webo_thumb_webo ────→ vid_web_video_web (1-to-1 logical mapping)
                      └─ Denormalized by category
```

---

## QUERY EXAMPLES

### Authentication Queries

```sql
-- User Login
SELECT * FROM accounts_user WHERE username = 'john_doe';

-- User Registration Check
SELECT COUNT(*) FROM accounts_user WHERE email = 'john@example.com';
```

### Content Retrieval Queries

```sql
-- Homepage Content (Random Order)
SELECT * FROM hume_thumb ORDER BY RANDOM();

-- Search Content
SELECT * FROM hume_thumb WHERE title LIKE 'python%' ORDER BY RANDOM();

-- Get Video Details
SELECT * FROM videos_video WHERE id = 1;

-- Get AI/ML Content
SELECT * FROM vid_aiml_video_aiml ORDER BY date DESC LIMIT 10;

-- Get Cybersecurity Content
SELECT * FROM vid_cyber_video_cyber ORDER BY date DESC LIMIT 10;

-- Get Web Development Content
SELECT * FROM vid_web_video_web ORDER BY date DESC LIMIT 10;
```

### Content Management Queries

```sql
-- Save New Content (Dual Write)
INSERT INTO hume_thumb (title, dinak, thumbnail_image)
VALUES ('Python Basics', '2024-01-15', 'media/thumbnail/python.jpg');

INSERT INTO videos_video (title, video_file, text, image, date)
VALUES ('Python Basics', 'media/vid/python.mp4', '<p>Content</p>',
        'media/photo/python.jpg', datetime('now'));

-- Update Content
UPDATE hume_thumb SET title = 'Python Advanced' WHERE id = 1;
UPDATE videos_video SET text = '<p>Updated content</p>' WHERE id = 1;

-- Delete Content
DELETE FROM hume_thumb WHERE id = 1;
DELETE FROM videos_video WHERE id = 1;
```

### Reporting Queries

```sql
-- Total Users
SELECT COUNT(*) as total_users FROM accounts_user;

-- Total Content Items
SELECT
    'hume' as category, COUNT(*) as count FROM hume_thumb
UNION ALL
SELECT 'aimlo', COUNT(*) FROM aimlo_thumb_aimlo
UNION ALL
SELECT 'cybero', COUNT(*) FROM cybero_thumb_cybero
UNION ALL
SELECT 'webo', COUNT(*) FROM webo_thumb_webo;

-- Total Videos
SELECT
    'general' as category, COUNT(*) FROM videos_video
UNION ALL
SELECT 'aiml', COUNT(*) FROM vid_aiml_video_aiml
UNION ALL
SELECT 'cyber', COUNT(*) FROM vid_cyber_video_cyber
UNION ALL
SELECT 'web', COUNT(*) FROM vid_web_video_web;

-- Recent Uploads
SELECT title, date FROM videos_video ORDER BY date DESC LIMIT 5;

-- Content by Date Range
SELECT * FROM hume_thumb
WHERE dinak BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY dinak;
```

---

## FIELD TYPE SPECIFICATIONS

### BigAutoField

- Type: Integer (64-bit)
- Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
- Auto-increment starting from 1
- Primary key unique constraint

### CharField

- Type: Text (variable length)
- Max length defined in field
- Indexed for search performance
- Supports case-insensitive filtering

### EmailField

- Type: Text
- Validated email format (RFC 5322)
- Inherits from CharField(254)
- Unique constraint applied

### DateField

- Type: Date (YYYY-MM-DD)
- Stored as ISO format
- No time component
- Used for batch grouping

### DateTimeField

- Type: DateTime (YYYY-MM-DD HH:MM:SS.ffffff)
- Includes timezone support (if USE_TZ=True)
- auto_now_add=True sets creation timestamp
- Sorted for chronological ordering

### FileField

- Type: Text (path reference)
- Stores relative path to media directory
- max_length=250 limits path depth
- null=True allows optional files
- default=None for empty values

### ImageField

- Type: Text (path reference)
- Inherits from FileField
- Validates image format
- Stores in media/photo/ directory
- Optional for video thumbnails

### HTMLField (TinyMCE)

- Type: Text (unlimited)
- Supports rich HTML formatting
- Editor: TinyMCE rich text editor
- Sanitized on display (security)
- Stores complete HTML markup

---

## DATA VOLUME ESTIMATES

### Current Deployment

```
Assumed Content:
├── hume_thumb: ~50 records
├── aimlo_thumb_aimlo: ~30 records
├── cybero_thumb_cybero: ~25 records
├── webo_thumb_webo: ~20 records
├── videos_video: ~50 records
├── vid_aiml_video_aiml: ~30 records
├── vid_cyber_video_cyber: ~25 records
├── vid_web_video_web: ~20 records
└── accounts_user: ~10-100 records (development)

Total Database Size: ~50-100 MB (with video files: ~50-200 GB)
```

### Scalability Limits (SQLite3)

- Maximum database file size: ~1 TB
- Recommended concurrent users: < 10-20
- Performance optimization needed beyond: ~100k records

---

## DATA INTEGRITY NOTES

### Denormalization Pattern

```
Current Design Pattern:

Traditional Normalized:
├─ content_base
│  ├─ id, title, date
│  └─ category_id (FK)
└─ categories
   └─ id, name

Current Denormalized:
├─ hume_thumb (main)
├─ aimlo_thumb_aimlo (ai/ml)
├─ cybero_thumb_cybero (security)
├─ webo_thumb_webo (web)
├─ videos_video (main)
├─ vid_aiml_video_aiml (ai/ml)
├─ vid_cyber_video_cyber (security)
└─ vid_web_video_web (web)

Advantages: Category-specific optimization, independent scaling
Disadvantages: Sync challenges, code duplication, consistency issues
```

### Data Consistency Considerations

```
Issue: Thumbnail + Video storage in separate tables
Solution: Manual synchronization required in /saveenquiry view

Current Implementation (2-table write):
1. INSERT INTO hume_thumb (title, dinak, thumbnail_image)
2. INSERT INTO videos_video (title, video_file, text, image)

Synchronization Challenge: No foreign key relationship
Risk: Orphaned records if second insert fails
```

---

## MIGRATION HISTORY

```
Database Migrations:

accounts/
  └─ 0001_initial.py - Create User model
  └─ 0002_alter_user_password.py - Modify password field

aimlo/
  └─ 0001_initial.py - Create thumb_aimlo model

cybero/
  └─ 0001_initial.py - Create thumb_cybero model

home/
  └─ 0001_initial.py - Create thumb model (hume)
  └─ 0002_thumb_thumbnail_image.py - Add thumbnail field

videos/
  └─ (Auto-generated) - Create Video model
  └─ (Auto-generated) - Create Video_aiml, Video_cyber, Video_web models

Other apps:
  └─ (Empty) - No custom models (makemigrations, migrate, etc.)
```

---

## PERFORMANCE INDEXES

### Recommended Indexes

```
-- Search Performance
CREATE INDEX idx_hume_title ON hume_thumb(title);
CREATE INDEX idx_aimlo_title ON aimlo_thumb_aimlo(title);
CREATE INDEX idx_cybero_title ON cybero_thumb_cybero(title);
CREATE INDEX idx_webo_title ON webo_thumb_webo(title);

-- Video Search
CREATE INDEX idx_videos_title ON videos_video(title);
CREATE INDEX idx_vidaiml_title ON vid_aiml_video_aiml(title);
CREATE INDEX idx_vidcyber_title ON vid_cyber_video_cyber(title);
CREATE INDEX idx_vidweb_title ON vid_web_video_web(title);

-- Date Range Queries
CREATE INDEX idx_hume_date ON hume_thumb(dinak);
CREATE INDEX idx_videos_date ON videos_video(date);

-- User Queries
CREATE INDEX idx_user_username ON accounts_user(username);
CREATE INDEX idx_user_email ON accounts_user(email);
```

---

## DATABASE CONNECTION SETTINGS

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # SQLite3 specific settings
        'ATOMIC_REQUESTS': False,  # Can enable for data consistency
        'AUTOCOMMIT': True,        # Auto-commit transactions
        'TIMEOUT': 20,             # Connection timeout in seconds
    }
}
```

---

## BACKUP & RECOVERY

### Backup Strategy

```bash
# Single file backup (SQLite advantage)
cp db.sqlite3 db.sqlite3.backup

# Automatic backup with timestamp
cp db.sqlite3 db.sqlite3.$(date +%Y%m%d_%H%M%S).backup

# Backup with media files
tar -czf matrix_backup_$(date +%Y%m%d).tar.gz db.sqlite3 media/

# Database dump
python manage.py dumpdata > matrix_dump.json
```

### Recovery

```bash
# Restore database
cp db.sqlite3.backup db.sqlite3

# Restore from JSON dump
python manage.py loaddata matrix_dump.json
```

---

## DOCUMENTATION METADATA

- **Database Engine**: SQLite3
- **Python ORM**: Django ORM
- **Total Tables**: 9
- **Total Models**: 9
- **Total Fields**: 49 (across all tables)
- **File Upload Support**: Yes (FileField, ImageField)
- **Rich Text Support**: Yes (HTMLField - TinyMCE)
- **Authentication**: Custom User model
- **Session Management**: Django sessions
- **Transaction Support**: Limited (SQLite3)

---

**Last Updated:** May 25, 2026  
**Database Engine:** SQLite3  
**Django Version:** 5.0  
**Python Version:** 3.x
