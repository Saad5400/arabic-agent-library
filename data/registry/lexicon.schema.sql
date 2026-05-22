PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  title_normalized TEXT NOT NULL,
  author TEXT,
  author_normalized TEXT,
  category TEXT,
  source_type TEXT,
  language_stage TEXT,
  original_url TEXT,
  notes TEXT,
  registry_json TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lexicon_entries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_id TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
  source_entry_id TEXT,
  headword TEXT NOT NULL,
  headword_normalized TEXT NOT NULL,
  root TEXT,
  root_normalized TEXT,
  entry_text TEXT NOT NULL,
  entry_text_normalized TEXT NOT NULL,
  definition_summary TEXT,
  definition_summary_normalized TEXT,
  usage_notes TEXT,
  usage_notes_normalized TEXT,
  examples_json TEXT NOT NULL DEFAULT '[]',
  metadata_json TEXT NOT NULL DEFAULT '{}',
  provenance_json TEXT NOT NULL DEFAULT '{}',
  page_start INTEGER,
  page_end INTEGER,
  section_ref TEXT,
  sort_key TEXT NOT NULL,
  content_sha256 TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(source_id, source_entry_id),
  UNIQUE(source_id, headword_normalized, content_sha256)
);

CREATE INDEX IF NOT EXISTS idx_lexicon_entries_source_id ON lexicon_entries(source_id);
CREATE INDEX IF NOT EXISTS idx_lexicon_entries_headword_normalized ON lexicon_entries(headword_normalized);
CREATE INDEX IF NOT EXISTS idx_lexicon_entries_root_normalized ON lexicon_entries(root_normalized);
CREATE INDEX IF NOT EXISTS idx_lexicon_entries_sort_key ON lexicon_entries(sort_key);

CREATE VIRTUAL TABLE IF NOT EXISTS lexicon_entries_fts USING fts5(
  headword,
  headword_normalized,
  root,
  root_normalized,
  definition_summary,
  definition_summary_normalized,
  entry_text,
  entry_text_normalized,
  content='lexicon_entries',
  content_rowid='id',
  tokenize='unicode61 remove_diacritics 2'
);

CREATE TRIGGER IF NOT EXISTS lexicon_entries_ai AFTER INSERT ON lexicon_entries BEGIN
  INSERT INTO lexicon_entries_fts(
    rowid,
    headword,
    headword_normalized,
    root,
    root_normalized,
    definition_summary,
    definition_summary_normalized,
    entry_text,
    entry_text_normalized
  ) VALUES (
    new.id,
    new.headword,
    new.headword_normalized,
    new.root,
    new.root_normalized,
    new.definition_summary,
    new.definition_summary_normalized,
    new.entry_text,
    new.entry_text_normalized
  );
END;

CREATE TRIGGER IF NOT EXISTS lexicon_entries_ad AFTER DELETE ON lexicon_entries BEGIN
  INSERT INTO lexicon_entries_fts(
    lexicon_entries_fts,
    rowid,
    headword,
    headword_normalized,
    root,
    root_normalized,
    definition_summary,
    definition_summary_normalized,
    entry_text,
    entry_text_normalized
  ) VALUES (
    'delete',
    old.id,
    old.headword,
    old.headword_normalized,
    old.root,
    old.root_normalized,
    old.definition_summary,
    old.definition_summary_normalized,
    old.entry_text,
    old.entry_text_normalized
  );
END;

CREATE TRIGGER IF NOT EXISTS lexicon_entries_au AFTER UPDATE ON lexicon_entries BEGIN
  INSERT INTO lexicon_entries_fts(
    lexicon_entries_fts,
    rowid,
    headword,
    headword_normalized,
    root,
    root_normalized,
    definition_summary,
    definition_summary_normalized,
    entry_text,
    entry_text_normalized
  ) VALUES (
    'delete',
    old.id,
    old.headword,
    old.headword_normalized,
    old.root,
    old.root_normalized,
    old.definition_summary,
    old.definition_summary_normalized,
    old.entry_text,
    old.entry_text_normalized
  );
  INSERT INTO lexicon_entries_fts(
    rowid,
    headword,
    headword_normalized,
    root,
    root_normalized,
    definition_summary,
    definition_summary_normalized,
    entry_text,
    entry_text_normalized
  ) VALUES (
    new.id,
    new.headword,
    new.headword_normalized,
    new.root,
    new.root_normalized,
    new.definition_summary,
    new.definition_summary_normalized,
    new.entry_text,
    new.entry_text_normalized
  );
END;
