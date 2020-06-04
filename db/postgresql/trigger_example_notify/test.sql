
DROP TRIGGER IF EXISTS "test" ON "events";
DROP FUNCTION IF EXISTS inotify;


CREATE FUNCTION inotify() 
    RETURNS TRIGGER AS 
    $$
    DECLARE
        fkuid INTEGER;
    BEGIN
        SELECT uid INTO fkuid FROM users WHERE fk_gid = 1;
        INSERT INTO notify(fk_evtid, fk_uid, read) 
            VALUES (NEW.id, fkuid, False);

        RETURN NEW;
    END;
    $$ LANGUAGE PLpgSQL;


CREATE TRIGGER "test" 
    AFTER INSERT 
    ON "events"
    FOR EACH ROW 
    EXECUTE PROCEDURE inotify();
