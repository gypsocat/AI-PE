--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: loading_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.loading_table (
    id bigint NOT NULL,
    code character varying(20) NOT NULL,
    user_identity character varying(8) NOT NULL,
    CONSTRAINT loading_table_user_identity_check CHECK (((user_identity)::text = ANY ((ARRAY['teacher'::character varying, 'student'::character varying])::text[])))
);


ALTER TABLE public.loading_table OWNER TO postgres;

--
-- Name: sport1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sport1 (
    studentid bigint NOT NULL,
    "time" timestamp without time zone NOT NULL,
    sportnumber integer NOT NULL,
    standrednumber integer NOT NULL,
    errornumber1 integer NOT NULL,
    errornumber2 integer NOT NULL,
    sporttime character varying(16) NOT NULL,
    studentclass integer NOT NULL,
    grade integer NOT NULL
);


ALTER TABLE public.sport1 OWNER TO postgres;

--
-- Name: sport_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sport_records (
    "time" timestamp without time zone NOT NULL,
    sport_type character varying(100),
    score numeric(10,2),
    detail bigint
);


ALTER TABLE public.sport_records OWNER TO postgres;

--
-- Name: student_message; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_message (
    studentid bigint NOT NULL,
    name character varying(255) NOT NULL,
    sex integer NOT NULL,
    class integer NOT NULL,
    term integer NOT NULL
);


ALTER TABLE public.student_message OWNER TO postgres;

--
-- Name: teacher_message; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher_message (
    teacherid bigint NOT NULL,
    name character varying(20) NOT NULL,
    class1 integer,
    term1 integer,
    class2 integer,
    term2 integer,
    class3 integer,
    term3 integer
);


ALTER TABLE public.teacher_message OWNER TO postgres;

--
-- Name: 仰卧起坐; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."仰卧起坐" (
    studentid bigint,
    "time" timestamp without time zone,
    sportnumber integer,
    standrednumber integer,
    errornumber1 integer,
    errornumber2 integer,
    sporttime character varying(16),
    studentclass integer,
    grade integer
);


ALTER TABLE public."仰卧起坐" OWNER TO postgres;

--
-- Name: 引体向上; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."引体向上" (
    studentid bigint NOT NULL,
    "time" timestamp without time zone NOT NULL,
    sportnumber integer,
    standrednumber integer,
    errornumber1 integer,
    errornumber2 integer,
    sporttime character varying(16),
    studentclass integer,
    grade integer
);


ALTER TABLE public."引体向上" OWNER TO postgres;

--
-- Name: 深蹲; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."深蹲" (
    studentid bigint,
    "time" timestamp without time zone,
    sportnumber integer,
    standrednumber integer,
    errornumber1 integer,
    errornumber2 integer,
    sporttime integer,
    studentclass integer,
    grade integer
);


ALTER TABLE public."深蹲" OWNER TO postgres;

--
-- Name: 立定跳远; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."立定跳远" (
    studentid bigint,
    "time" character varying(255),
    sportnumber integer,
    standrednumber integer,
    errornumber1 integer,
    errornumber2 integer,
    sporttime integer,
    studentclass integer,
    grade integer
);


ALTER TABLE public."立定跳远" OWNER TO postgres;

--
-- Name: 跳绳; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."跳绳" (
    studentid bigint,
    "time" timestamp without time zone,
    sportnumber integer,
    standrednumber integer,
    errornumber1 integer,
    errornumber2 integer,
    sporttime character varying(16),
    studentclass integer,
    grade integer
);


ALTER TABLE public."跳绳" OWNER TO postgres;

--
-- Data for Name: loading_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.loading_table (id, code, user_identity) FROM stdin;
1601020	123456a	student
1601008	hxy	student
888	654321	teacher
889	aaaaa	teacher
\.


--
-- Data for Name: sport1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sport1 (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
\.


--
-- Data for Name: sport_records; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sport_records ("time", sport_type, score, detail) FROM stdin;
2024-01-01 09:00:00	引体向上	85.20	1601008
2024-01-20 10:00:00	俯卧撑	45.90	1601008
2024-02-05 10:30:00	仰卧起坐	32.40	1601020
2024-02-15 11:00:00	跳绳	78.30	1601008
2024-03-05 12:00:00	跑步	66.70	1601008
2024-03-15 12:30:00	引体向上	79.80	1601020
2024-03-25 13:00:00	仰卧起坐	95.20	1601008
2024-03-27 13:30:00	跳绳	87.40	1601020
2024-01-10 09:30:00	引体向上	57.60	1601020
2024-02-25 11:30:00	立定跳远	89.10	1601020
\.


--
-- Data for Name: student_message; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_message (studentid, name, sex, class, term) FROM stdin;
1601020	吴卓峻	0	1601	4
1601008	胡翔越	0	1601	4
\.


--
-- Data for Name: teacher_message; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher_message (teacherid, name, class1, term1, class2, term2, class3, term3) FROM stdin;
888	曾勇	1601	1	1602	1	1603	1
889	高中喜	1604	1	1605	1	1606	1
\.


--
-- Data for Name: 仰卧起坐; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."仰卧起坐" (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
1601008	2024-01-20 10:00:00	1	85	0	0	16.50	1	22
1601008	2024-03-25 13:00:00	2	95	0	0	20.03	2	22
\.


--
-- Data for Name: 引体向上; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."引体向上" (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
1601008	2024-01-01 09:00:00	1	1	0	0	13分钟	1	10
1601020	2024-01-10 09:30:00	2	2	0	0	10分钟	2	11
1601020	2024-03-15 12:30:00	8	8	0	0	21分钟	2	11
\.


--
-- Data for Name: 深蹲; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."深蹲" (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
\.


--
-- Data for Name: 立定跳远; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."立定跳远" (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
1601020	2024-02-25 11:30:00	1	100	5	3	90	2024	3
\.


--
-- Data for Name: 跳绳; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."跳绳" (studentid, "time", sportnumber, standrednumber, errornumber1, errornumber2, sporttime, studentclass, grade) FROM stdin;
\.


--
-- Name: loading_table loading_table_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.loading_table
    ADD CONSTRAINT loading_table_code_key UNIQUE (code);


--
-- Name: loading_table loading_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.loading_table
    ADD CONSTRAINT loading_table_pkey PRIMARY KEY (id);


--
-- Name: 引体向上 pk_studentid_time; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."引体向上"
    ADD CONSTRAINT pk_studentid_time PRIMARY KEY (studentid, "time");


--
-- Name: sport1 sport1_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sport1
    ADD CONSTRAINT sport1_pk PRIMARY KEY (studentid, "time");


--
-- Name: sport_records sport_records_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sport_records
    ADD CONSTRAINT sport_records_pkey PRIMARY KEY ("time");


--
-- Name: student_message student_message_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_message
    ADD CONSTRAINT student_message_pkey PRIMARY KEY (studentid);


--
-- Name: teacher_message teacher_message_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_message
    ADD CONSTRAINT teacher_message_pkey PRIMARY KEY (teacherid);


--
-- Name: sport_records sport_records_detail_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sport_records
    ADD CONSTRAINT sport_records_detail_fkey FOREIGN KEY (detail) REFERENCES public.student_message(studentid);


--
-- PostgreSQL database dump complete
--

