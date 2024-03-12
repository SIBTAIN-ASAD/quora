// Functions to handle authentication

import axios from "axios";

import { AUTH_URLS } from "../constants/constants";

// Function to handle user authentication
export const login = async (username, password) => {
  try {
    const response = await axios.post(AUTH_URLS.LOGIN, { username, password });
    const { access_token, refresh_token } = response.data;
    localStorage.setItem("token", access_token);
    localStorage.setItem("refresh_token", refresh_token);
    return response.data.user;
  } catch (error) {
    console.error("Error logging in:", error.message);
    throw error;
  }
};

// Function to check if user is logged in or not
// sometime token is expired but refresh token is still valid
// return boolean value
export const isLoggedIn = async () => {
  try {
    const token = localStorage.getItem("token");
    if (token) {
      const response = await axios.get(AUTH_URLS.HOME, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (response.status === 200) {
        return true;
      }
    }
    return false;
  } catch (error) {
    return false;
  }
};

// refresh the access token if it is expired
export const refreshToken = async () => {
  try {
    const refresh_token = localStorage.getItem("refresh_token");
    if (refresh_token) {
      const response = await axios.post(AUTH_URLS.REFRESH, { refresh_token });
      const { access_token } = response.data;
      localStorage.setItem("token", access_token);
    }
  } catch (error) {
    console.error("Error refreshing access token:", error.message);
    throw error;
  }
};


// Function to handle user logout
export const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("refresh_token");
};

// Function to fetch user data
export const fetchUserData = async () => {
  try {
    const token = localStorage.getItem("token");
    if (token) {
      const response = await axios.get(AUTH_URLS.HOME, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    }
  } catch (error) {
    console.error("Error fetching user data:", error.message);
    // set token to null if error occurs
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
    throw error;
  }
};

// Function to refresh the access token
export const refreshAccessToken = async () => {
  try {
    const refresh_token = localStorage.getItem("refresh_token");
    if (refresh_token) {
      const response = await axios.post(AUTH_URLS.REFRESH, { refresh_token });
      const { access_token } = response.data;
      localStorage.setItem("token", access_token);
    }
  } catch (error) {
    console.error("Error refreshing access token:", error.message);
    throw error;
  }
};
