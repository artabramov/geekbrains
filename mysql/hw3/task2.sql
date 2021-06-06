CREATE TABLE IF NOT EXISTS likes (
    id          BIGINT(20)   UNSIGNED NOT NULL AUTO_INCREMENT,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id     BIGINT(20)   UNSIGNED NOT NULL,
    parent_type ENUM('users', 'media', 'photos') NOT NULL,
    parent_id   BIGINT(20)   UNSIGNED NOT NULL,

    PRIMARY KEY (id),
            KEY (created_at),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
     UNIQUE KEY (user_id, parent_type, parent_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
