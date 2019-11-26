-- returns the record of second table
-- checks second_table
ALTER SCHEMA hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table change name name  varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
