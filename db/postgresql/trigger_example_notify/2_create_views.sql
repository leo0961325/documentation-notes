
-- Table 建完後再用這個


DROP VIEW IF EXISTS "v_notify";

CREATE VIEW "v_notify" AS
    SELECT 
        ee.fk_etype "severity", 
        ee.id "evtid",
        ee.content "content", 
        ee.dt "dt", 
        uu.uid, 
        uu.username "user", 
        nt.read "read"
    FROM "notify" nt 
        LEFT OUTER JOIN "users" uu   ON  nt.fk_uid = uu.uid
        LEFT OUTER JOIN "events" ee  ON  nt.fk_evtid = ee.id;


-- 使用範例

SELECT * FROM "v_notify";
SELECT * FROM "v_notify" WHERE "read" = FALSE;
SELECT * FROM "v_notify" WHERE "read" = TRUE;

