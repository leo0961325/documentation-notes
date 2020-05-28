-- 未完成

DROP TRIGGER IF EXISTS "inotify" ON "events";
DROP FUNCTION IF EXISTS "pfnotify";


CREATE FUNCTION pfnotify() 
    RETURNS TRIGGER AS 
    $$
    DECLARE
		vvgid INTEGER;
    BEGIN
        SELECT uid INTO vvuid FROM users WHERE fk_gid = vvgid;
        INSERT INTO notify(fk_evtid, fk_uid, read) 
            VALUES (NEW.id, vvuid, False);

        RETURN NEW;
    END;
    $$ LANGUAGE PLpgSQL;


CREATE TRIGGER "inotify" 
    AFTER INSERT 
    ON "events"
    FOR EACH ROW 
    EXECUTE PROCEDURE pfnotify();

DELETE FROM notify;
DELETE FROM events;
INSERT INTO "events" ("fk_etype", "dt", "content") VALUES ('fatal',  NOW(),    '嚴重錯誤阿!!! XXX怎麼了!');