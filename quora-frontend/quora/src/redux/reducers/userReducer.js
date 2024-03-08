import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchUserData } from '../../services/authAPIs';

// Async thunk action creator to fetch user details after login
export const fetchUserDetails = createAsyncThunk(
  'user/fetchUserDetails',
  async () => {
    const user = await fetchUserData();
    return user;
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    userDetails: null,
    loading: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchUserDetails.pending, (state) => {
        state.loading = 'pending';
      })
      .addCase(fetchUserDetails.fulfilled, (state, action) => {
        state.loading = 'idle';
        state.userDetails = action.payload;
      })
      .addCase(fetchUserDetails.rejected, (state, action) => {
        state.loading = 'idle';
        state.error = action.error.message;
      });
  },
});

export default userSlice.reducer;
