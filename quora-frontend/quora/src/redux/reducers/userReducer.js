import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchUserData } from "../../services/authAPIs";

// Async thunk action creator to fetch user details after login
export const fetchUserDetails = createAsyncThunk(
  "user/fetchUserDetails", // Action type
  async () => {
    // Payload creator
    const user = await fetchUserData(); // Call fetchUserData function
    return user;
  }
);

const userSlice = createSlice({
  name: "user",
  initialState: {
    userDetails: null,
    loading: "start",
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchUserDetails.pending, (state) => {
      state.loading = "pending";
    });
    builder.addCase(fetchUserDetails.fulfilled, (state, action) => {
      state.loading = "idle";
      state.userDetails = action.payload;
    });
    builder.addCase(fetchUserDetails.rejected, (state, action) => {
      state.loading = "idle";
      state.error = action.error.message;
    });
  },
});

export default userSlice.reducer;
