// This file will configure the redux store with thunk middleware and export it.

import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../reducers/userReducer";

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

export default store;
