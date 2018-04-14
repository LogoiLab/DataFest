CREATE TABLE jobs (
    date DATE NOT NULL, -- 4
    companyId TEXT, -- 0
    jobId TEXT, -- 0
    country CHAR(2) NOT NULL, -- 1
    stateProvince CHAR(2) NOT NULL, -- 0
    city TEXT NOT NULL, -- 0
    avgOverallRating FLOAT NOT NULL, -- 2
    numReviews INTEGER, -- 2
    industry TEXT, -- 1
    normTitle TEXT, -- 1
    normTitleCategory TEXT, -- 1
    descriptionCharacterLength INTEGER NOT NULL, -- 2
    descriptionWordCount INTEGER NOT NULL, -- 2
    experienceRequired INTEGER NOT NULL, -- 2
    estimatedSalary INTEGER, -- 2
    salaryCurrency TEXT, -- 0
    jobLanguage TEXT NOT NULL, -- 0
    supervisingJob INTEGER NOT NULL, -- 3
    licenseRequiredJob INTEGER NOT NULL, -- 3
    educationRequirements TEXT, -- 1
    jobAgeDays INTEGER NOT NULL, -- 2
    clicks INTEGER NOT NULL, -- 2
    localClicks INTEGER NOT NULL, -- 2
    id INTEGER PRIMARY KEY AUTOINCREMENT
)
-- 33
-- 54110559/14586035 = 3.7
-- +
-- 36.7
