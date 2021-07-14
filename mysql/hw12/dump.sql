-- users

CREATE TYPE user_status AS ENUM ('pending', 'approved', 'trash');

CREATE TABLE IF NOT EXISTS users (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    remind_date TIMESTAMP NOT NULL,
    user_status user_status,
    user_token  CHAR(80) NOT NULL UNIQUE,
    user_email  VARCHAR(255) NOT NULL UNIQUE,
    user_hash   VARCHAR(40) NOT NULL,
    user_name   VARCHAR(128) NOT NULL
);

-- users meta

CREATE TABLE IF NOT EXISTS users_meta (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    user_id     BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    meta_key    VARCHAR(20)  NOT NULL,
    meta_value  VARCHAR(255) NOT NULL,
    CONSTRAINT user_meta_uid UNIQUE(user_id, meta_key)
);

-- hubs

CREATE TYPE hub_status AS ENUM ('custom', 'trash');

CREATE TABLE IF NOT EXISTS hubs (
    id         BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    user_id     BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    hub_status hub_status NOT NULL,
    hub_name   VARCHAR(128) NOT NULL
);

-- hubs meta

CREATE TABLE IF NOT EXISTS hubs_meta (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    hub_id      BIGSERIAL REFERENCES hubs(id) ON DELETE CASCADE NOT NULL,
    meta_key    VARCHAR(20)  NOT NULL,
    meta_value  VARCHAR(255) NOT NULL,
    CONSTRAINT hub_meta_uid UNIQUE(hub_id, meta_key)
);

-- users roles

CREATE TYPE role_status AS ENUM ('admin', 'editor', 'reader');

CREATE TABLE IF NOT EXISTS users_roles (
    id         BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    user_id     BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    hub_id      BIGSERIAL REFERENCES hubs(id) ON DELETE CASCADE NOT NULL,
    role_status role_status NOT NULL,
    CONSTRAINT user_role_uid UNIQUE(user_id, hub_id)
);

-- posts

CREATE TYPE post_status AS ENUM ('todo', 'doing', 'done', 'trash');

CREATE TABLE IF NOT EXISTS posts (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    user_id     BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    hub_id      BIGSERIAL REFERENCES hubs(id) ON DELETE CASCADE NOT NULL,
    post_status post_status NOT NULL,
    post_title  VARCHAR(255) NOT NULL
);

-- post tags

CREATE TABLE IF NOT EXISTS posts_tags (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    post_id     BIGSERIAL REFERENCES posts(id) ON DELETE CASCADE NOT NULL,
    tag_value   VARCHAR(255) NOT NULL,
    CONSTRAINT post_tag_uid UNIQUE(post_id, tag_value)
);

-- posts meta

CREATE TABLE IF NOT EXISTS posts_meta (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    post_id     BIGSERIAL REFERENCES posts(id) ON DELETE CASCADE NOT NULL,
    meta_key    VARCHAR(20)  NOT NULL,
    meta_value  VARCHAR(255) NOT NULL,
    CONSTRAINT post_meta_uid UNIQUE(post_id, meta_key)
);

-- posts comments

CREATE TABLE IF NOT EXISTS posts_comments (
    id              BIGSERIAL NOT NULL PRIMARY KEY,
    create_date     TIMESTAMP NOT NULL,
    update_date     TIMESTAMP NOT NULL,
    user_id         BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    post_id         BIGSERIAL REFERENCES posts(id) ON DELETE CASCADE NOT NULL,
    comment_content TEXT NOT NULL
);

-- uploads

CREATE TABLE IF NOT EXISTS uploads (
    id          BIGSERIAL NOT NULL PRIMARY KEY,
    create_date TIMESTAMP NOT NULL,
    update_date TIMESTAMP NOT NULL,
    user_id     BIGSERIAL REFERENCES users(id) ON DELETE NO ACTION NOT NULL,
    comment_id  BIGSERIAL REFERENCES posts_comments(id) ON DELETE SET NULL,
    upload_name VARCHAR(255) NOT NULL,
    upload_file VARCHAR(255) NOT NULL UNIQUE,
    upload_mime VARCHAR(255) NOT NULL,
    upload_size INT NOT NULL
);


-- drop all

DROP TABLE IF EXISTS users_meta;
DROP TABLE IF EXISTS users_roles;
DROP TABLE IF EXISTS hubs_meta;
DROP TABLE IF EXISTS posts_meta;
DROP TABLE IF EXISTS posts_tags;
DROP TABLE IF EXISTS posts_comments;
DROP TABLE IF EXISTS uploads;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS hubs;
DROP TABLE IF EXISTS users;

DROP TYPE IF EXISTS user_status;
DROP TYPE IF EXISTS hub_status;
DROP TYPE IF EXISTS role_status;
DROP TYPE IF EXISTS post_status;

-- truncate all

TRUNCATE TABLE users_meta;
TRUNCATE TABLE users_roles;
TRUNCATE TABLE hubs_meta;
TRUNCATE TABLE posts_meta;
TRUNCATE TABLE posts_tags;
TRUNCATE TABLE posts_comments;
TRUNCATE TABLE uploads;
TRUNCATE TABLE posts;
TRUNCATE TABLE hubs;
TRUNCATE TABLE users;

-- select all

\pset format wrapped
SELECT * FROM users; SELECT * FROM users_meta; SELECT * FROM users_roles; SELECT * FROM hubs; SELECT * FROM hubs_meta; SELECT * FROM posts; SELECT * FROM posts_meta; SELECT * FROM posts_tags; SELECT * FROM posts_comments; SELECT * FROM uploads; 

-- test data

INSERT INTO users (user_status, user_token, user_email, user_hash, user_name) VALUES ('pending', '01234567890123456789012345678901234567890123456789012345678901234567890123456789', 'noreply@noreply.no', '0123456789012345678901234567890123456789', 'noname');
INSERT INTO users_meta (user_id, meta_key, meta_value) VALUES (1, 'key1', 'value1');
INSERT INTO users_meta (user_id, meta_key, meta_value) VALUES (1, 'key2', 'value2');
INSERT INTO hubs (user_id, hub_status, hub_name) VALUES (1, 'custom', 'hubname');
INSERT INTO hubs_meta (hub_id, meta_key, meta_value) VALUES (1, 'hkey1', 'hvalue1');
INSERT INTO users_roles (user_id, hub_id, role_status) VALUES (1, 1, 'admin');
INSERT INTO posts (user_id, hub_id, post_status, post_title) VALUES (1, 1, 'todo', 'Lorem ipsum');
INSERT INTO posts_meta (post_id, meta_key, meta_value) VALUES (1, 'pkey1', 'pvalue1');
INSERT INTO posts_meta (post_id, meta_key, meta_value) VALUES (1, 'pkey2', 'pvalue2');
INSERT INTO posts_comments (post_id, user_id, comment_content) VALUES (1, 1, 'Dolores sit amet');
INSERT INTO uploads (comment_id, user_id, upload_name, upload_file, upload_mime, upload_size) VALUES (1, 1, 'Upload name', './path/file.ext', 'image/png', 100);

-- triggers

DELIMITER |
CREATE TRIGGER role_insert
AFTER INSERT
ON users_roles 
FOR EACH ROW 
BEGIN
    SET @roles_count := (SELECT COUNT(id) FROM users_roles WHERE hub_id = OLD.hub_id);
    IF EXISTS (SELECT id FROM meta WHERE parent_type = 'hubs' AND parent_id = NEW.hub_id AND meta_key='roles_count') THEN
        UPDATE hubs_meta SET meta_value=@roles_count WHERE hub_id = NEW.hub_id AND meta_key='roles_count';
    ELSE
        INSERT INTO hubs_meta (hub_id, meta_key, meta_value) VALUES (NEW.hub_id, 'roles_count', @roles_count);
    END IF;
END;
| 
DELIMITER ;


DELIMITER |
CREATE TRIGGER role_delete
AFTER DELETE
ON roles 
FOR EACH ROW 
BEGIN
    SET @roles_count := (SELECT COUNT(id) FROM roles WHERE hub_id = OLD.hub_id);
    IF @roles_count = 0 THEN
        DELETE FROM meta WHERE hub_id = OLD.hub_id AND meta_key = 'roles_count';
    ELSE
        UPDATE meta SET meta_value=@roles_count WHERE hub_id = OLD.hub_id AND meta_key='roles_count';
    END IF;
END;
| 
DELIMITER ;

