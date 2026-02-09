--
-- PostgreSQL database dump
--

\restrict Y7KaPpSeUUTM1zsTSuTnmebPVHEVTERhB7OdWxbmcvaOEw8mRKNbLRnWad9ZZac

-- Dumped from database version 16.10
-- Dumped by pg_dump version 16.10

-- Started on 2026-02-09 16:39:45

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
-- TOC entry 223 (class 1259 OID 228970)
-- Name: actions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actions (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.actions OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 228969)
-- Name: actions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.actions_id_seq OWNER TO postgres;

--
-- TOC entry 4972 (class 0 OID 0)
-- Dependencies: 222
-- Name: actions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actions_id_seq OWNED BY public.actions.id;


--
-- TOC entry 230 (class 1259 OID 229029)
-- Name: actions_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.actions ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.actions_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 225 (class 1259 OID 228981)
-- Name: permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permissions (
    id integer NOT NULL,
    service_id integer NOT NULL,
    action_id integer NOT NULL,
    description text
);


ALTER TABLE public.permissions OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 228980)
-- Name: permissions_new_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.permissions_new_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.permissions_new_id_seq OWNER TO postgres;

--
-- TOC entry 4974 (class 0 OID 0)
-- Dependencies: 224
-- Name: permissions_new_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.permissions_new_id_seq OWNED BY public.permissions.id;


--
-- TOC entry 227 (class 1259 OID 229026)
-- Name: permissions_new_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.permissions ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.permissions_new_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 226 (class 1259 OID 229001)
-- Name: role_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role_permissions (
    role_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.role_permissions OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 228948)
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 228947)
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roles_id_seq OWNER TO postgres;

--
-- TOC entry 4977 (class 0 OID 0)
-- Dependencies: 218
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- TOC entry 228 (class 1259 OID 229027)
-- Name: roles_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.roles ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.roles_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 228959)
-- Name: services; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.services (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.services OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 228958)
-- Name: services_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.services_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.services_id_seq OWNER TO postgres;

--
-- TOC entry 4979 (class 0 OID 0)
-- Dependencies: 220
-- Name: services_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.services_id_seq OWNED BY public.services.id;


--
-- TOC entry 229 (class 1259 OID 229028)
-- Name: services_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.services ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.services_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 228864)
-- Name: sessions_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sessions_users (
    session_id text NOT NULL,
    user_id bigint NOT NULL,
    refresh_token character varying(150) NOT NULL,
    user_agent character varying(200),
    ip character varying(45) NOT NULL,
    iat timestamp with time zone NOT NULL,
    exp timestamp with time zone NOT NULL
);


ALTER TABLE public.sessions_users OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 228854)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    first_name character varying(64) NOT NULL,
    date_register date DEFAULT (now())::date,
    email character varying(319) NOT NULL,
    passw character varying(150) NOT NULL,
    surname character varying(64) NOT NULL,
    last_name character varying(64) NOT NULL,
    is_active boolean DEFAULT true,
    role_id integer
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 228853)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4957 (class 0 OID 228970)
-- Dependencies: 223
-- Data for Name: actions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actions (id, name, description) FROM stdin;
1	read	Чтение данных
2	write	Запись данных
3	create	Создание записей
4	update	Обновление записей
5	delete	Удаление записей
6	deploy	Деплой приложений
7	manage	Управление ресурсами
8	read_salaries	Просмотр зарплат
9	read_security	Просмотр security events
\.


--
-- TOC entry 4959 (class 0 OID 228981)
-- Dependencies: 225
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permissions (id, service_id, action_id, description) FROM stdin;
1	1	1	Просмотр пользователей
2	1	3	Создание пользователей
3	1	4	Обновление пользователей
4	1	5	Удаление пользователей
5	2	1	Просмотр метрик и дашбордов
6	2	2	Создание отчетов
7	3	1	Просмотр серверов и логов
8	3	6	Деплой приложений
9	3	7	Управление серверами
10	4	1	Просмотр бюджетов
11	4	2	Управление расходами
12	4	8	Просмотр зарплат
13	5	1	Смотреть роли и привилегии
14	5	3	создавать роли и привилегии
\.


--
-- TOC entry 4960 (class 0 OID 229001)
-- Dependencies: 226
-- Data for Name: role_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.role_permissions (role_id, permission_id) FROM stdin;
1	1
7	1
8	1
1	2
7	2
1	3
1	4
1	5
5	5
3	5
2	5
4	5
1	6
5	6
4	6
1	7
3	7
2	7
4	7
8	7
1	8
3	8
2	8
1	9
2	9
1	10
6	10
4	10
1	11
6	11
1	12
6	12
7	12
1	13
1	14
\.


--
-- TOC entry 4953 (class 0 OID 228948)
-- Dependencies: 219
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id, name, description) FROM stdin;
1	admin	Администратор - полный доступ
2	devops	DevOps инженер - инфраструктура и деплой
3	developer	Разработчик - разработка и деплой
4	project_manager	Менеджер проектов - аналитика и планирование
5	data_analyst	Аналитик данных - аналитика и отчеты
6	finance_manager	Финансовый менеджер - бюджеты и расходы
7	hr	HR специалист - управление персоналом
8	security	Специалист по безопасности - аудит и мониторинг
\.


--
-- TOC entry 4955 (class 0 OID 228959)
-- Dependencies: 221
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.services (id, name, description) FROM stdin;
1	users	Управление пользователями
2	analytics	Аналитика и метрики
3	infrastructure	Инфраструктура и серверы
4	finance	Финансы и бюджеты
5	access matrix	Управление ролями и привилегиями
\.


--
-- TOC entry 4951 (class 0 OID 228864)
-- Dependencies: 217
-- Data for Name: sessions_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sessions_users (session_id, user_id, refresh_token, user_agent, ip, iat, exp) FROM stdin;
7a373803-9265-4897-8868-deb751fd884a	7	$argon2id$v=19$m=65536,t=3,p=4$zZkzxpiTkhLCuDdmLEVIqQ$JJCtr89cza8+e+GCnRwP8t+f2z+f4bslPyrvkA67iT0	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36	127.0.0.1	2026-02-08 14:13:17.800415+03	2026-03-10 14:13:17.800415+03
8491582c-549d-48ee-92f0-7048578fc9ce	26	$argon2id$v=19$m=65536,t=3,p=4$dS7F2Pv/P6cUgtA6JwQgxA$RI4AjWUEltpdWmGCdNW4EZ+svytlpqSlZGRof0lBc2k	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36	127.0.0.1	2026-02-09 12:53:59.924668+03	2026-03-11 12:53:59.924668+03
\.


--
-- TOC entry 4950 (class 0 OID 228854)
-- Dependencies: 216
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, first_name, date_register, email, passw, surname, last_name, is_active, role_id) FROM stdin;
2	a	2026-02-08	example@mail.ru	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	b	c	t	1
7	Evgeniya	2026-02-08	hr@example.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Ivanov	Ivannva	t	7
9	Admin	2026-02-08	admin@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	User	Adminovich	t	1
10	DevOps	2026-02-08	devops@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Engineer	Devopsov	t	2
11	John	2026-02-08	dev@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Developer	Doe	t	3
12	Jane	2026-02-08	pm@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Manager	Smith	t	4
13	Data	2026-02-08	analyst@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Analyst	Johnson	t	5
14	Finance	2026-02-08	finance@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Manager	Brown	t	6
15	HR	2026-02-08	hr@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Specialist	Wilson	t	7
16	Security	2026-02-08	security@company.com	$argon2id$v=19$m=65536,t=3,p=4$y9nb+z8H4HxPSSmFsPa+Nw$GQ9wN6vVRwldMzc8B+lHbq5ntwX995xDQHuVJmjxBPw	Officer	Davis	t	8
26	admin	2026-02-09	admin@example.com	$argon2id$v=19$m=65536,t=3,p=4$R4jROofQmtPaey8lBEAo5Q$Al5JtzjXntOsXhCdhty4w19UDGLZGNOCzhc6QLUwjAQ	adminov	Adminovich	t	1
25	Тестович	2026-02-09	testdev@example.com	$argon2id$v=19$m=65536,t=3,p=4$wrj3HkMIgVBqrbV2rrWWEg$YTQaBpPqZNrOxh18URIo9JWMj47S2XMmyYdnC58wETs	Тестов	Тест	f	3
\.


--
-- TOC entry 4982 (class 0 OID 0)
-- Dependencies: 222
-- Name: actions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actions_id_seq', 9, true);


--
-- TOC entry 4983 (class 0 OID 0)
-- Dependencies: 230
-- Name: actions_id_seq1; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actions_id_seq1', 9, true);


--
-- TOC entry 4984 (class 0 OID 0)
-- Dependencies: 224
-- Name: permissions_new_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.permissions_new_id_seq', 17, true);


--
-- TOC entry 4985 (class 0 OID 0)
-- Dependencies: 227
-- Name: permissions_new_id_seq1; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.permissions_new_id_seq1', 14, true);


--
-- TOC entry 4986 (class 0 OID 0)
-- Dependencies: 218
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 8, true);


--
-- TOC entry 4987 (class 0 OID 0)
-- Dependencies: 228
-- Name: roles_id_seq1; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq1', 8, true);


--
-- TOC entry 4988 (class 0 OID 0)
-- Dependencies: 220
-- Name: services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.services_id_seq', 6, true);


--
-- TOC entry 4989 (class 0 OID 0)
-- Dependencies: 229
-- Name: services_id_seq1; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.services_id_seq1', 5, true);


--
-- TOC entry 4990 (class 0 OID 0)
-- Dependencies: 215
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 26, true);


--
-- TOC entry 4788 (class 2606 OID 228979)
-- Name: actions actions_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT actions_name_key UNIQUE (name);


--
-- TOC entry 4790 (class 2606 OID 228977)
-- Name: actions actions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actions
    ADD CONSTRAINT actions_pkey PRIMARY KEY (id);


--
-- TOC entry 4793 (class 2606 OID 228988)
-- Name: permissions permissions_new_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_new_pkey PRIMARY KEY (id);


--
-- TOC entry 4795 (class 2606 OID 228990)
-- Name: permissions permissions_new_service_id_action_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_new_service_id_action_id_key UNIQUE (service_id, action_id);


--
-- TOC entry 4799 (class 2606 OID 229005)
-- Name: role_permissions role_permissions_new_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_new_pkey PRIMARY KEY (role_id, permission_id);


--
-- TOC entry 4780 (class 2606 OID 228957)
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- TOC entry 4782 (class 2606 OID 228955)
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- TOC entry 4784 (class 2606 OID 228968)
-- Name: services services_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_name_key UNIQUE (name);


--
-- TOC entry 4786 (class 2606 OID 228966)
-- Name: services services_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (id);


--
-- TOC entry 4774 (class 2606 OID 228870)
-- Name: sessions_users sessions_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions_users
    ADD CONSTRAINT sessions_users_pkey PRIMARY KEY (session_id);


--
-- TOC entry 4776 (class 2606 OID 228872)
-- Name: sessions_users sessions_users_refresh_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions_users
    ADD CONSTRAINT sessions_users_refresh_token_key UNIQUE (refresh_token);


--
-- TOC entry 4778 (class 2606 OID 228874)
-- Name: sessions_users sessions_users_session_id_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions_users
    ADD CONSTRAINT sessions_users_session_id_user_id_key UNIQUE (session_id, user_id);


--
-- TOC entry 4772 (class 2606 OID 228861)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 4791 (class 1259 OID 229018)
-- Name: idx_permissions_new_service_action; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_permissions_new_service_action ON public.permissions USING btree (service_id, action_id);


--
-- TOC entry 4796 (class 1259 OID 229017)
-- Name: idx_role_permissions_new_permission; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_role_permissions_new_permission ON public.role_permissions USING btree (permission_id);


--
-- TOC entry 4797 (class 1259 OID 229016)
-- Name: idx_role_permissions_new_role; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_role_permissions_new_role ON public.role_permissions USING btree (role_id);


--
-- TOC entry 4770 (class 1259 OID 228883)
-- Name: users_email_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX users_email_idx ON public.users USING btree (email) WITH (deduplicate_items='false') WHERE (is_active = true);


--
-- TOC entry 4802 (class 2606 OID 228996)
-- Name: permissions permissions_new_action_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_new_action_id_fkey FOREIGN KEY (action_id) REFERENCES public.actions(id) ON DELETE CASCADE;


--
-- TOC entry 4803 (class 2606 OID 228991)
-- Name: permissions permissions_new_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_new_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.services(id) ON DELETE CASCADE;


--
-- TOC entry 4804 (class 2606 OID 229011)
-- Name: role_permissions role_permissions_new_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_new_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.permissions(id) ON DELETE CASCADE;


--
-- TOC entry 4805 (class 2606 OID 229006)
-- Name: role_permissions role_permissions_new_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_permissions
    ADD CONSTRAINT role_permissions_new_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;


--
-- TOC entry 4801 (class 2606 OID 228875)
-- Name: sessions_users sessions_users_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sessions_users
    ADD CONSTRAINT sessions_users_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- TOC entry 4800 (class 2606 OID 229030)
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE SET NULL;


--
-- TOC entry 4970 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO crud_db_user;


--
-- TOC entry 4971 (class 0 OID 0)
-- Dependencies: 223
-- Name: TABLE actions; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.actions TO crud_db_user;


--
-- TOC entry 4973 (class 0 OID 0)
-- Dependencies: 225
-- Name: TABLE permissions; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.permissions TO crud_db_user;


--
-- TOC entry 4975 (class 0 OID 0)
-- Dependencies: 226
-- Name: TABLE role_permissions; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.role_permissions TO crud_db_user;


--
-- TOC entry 4976 (class 0 OID 0)
-- Dependencies: 219
-- Name: TABLE roles; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.roles TO crud_db_user;


--
-- TOC entry 4978 (class 0 OID 0)
-- Dependencies: 221
-- Name: TABLE services; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.services TO crud_db_user;


--
-- TOC entry 4980 (class 0 OID 0)
-- Dependencies: 217
-- Name: TABLE sessions_users; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.sessions_users TO crud_db_user;


--
-- TOC entry 4981 (class 0 OID 0)
-- Dependencies: 216
-- Name: TABLE users; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.users TO crud_db_user;


--
-- TOC entry 2070 (class 826 OID 228881)
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,INSERT,DELETE,UPDATE ON TABLES TO crud_db_user;


-- Completed on 2026-02-09 16:39:45

--
-- PostgreSQL database dump complete
--

\unrestrict Y7KaPpSeUUTM1zsTSuTnmebPVHEVTERhB7OdWxbmcvaOEw8mRKNbLRnWad9ZZac

