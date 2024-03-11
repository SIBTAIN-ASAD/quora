// File Contains all the constants used in the application

export const COMMENTS = 'http://localhost:8000/api/comment';

const AUTH_URLS = {
    LOGIN: 'http://localhost:8000/api/login',
    LOGOUT: 'http://localhost:8000/api/logout',
    HOME: 'http://localhost:8000/api/home'
}

Object.freeze(AUTH_URLS);

export { AUTH_URLS };
