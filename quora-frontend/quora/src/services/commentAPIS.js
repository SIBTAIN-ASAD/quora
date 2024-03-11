// File contains the helper function to fetch comments from the backend

import axios from "axios";
import { COMMENTS } from "../constants/constants";

export const fetchComments = async () => {
    try {
        const response = await axios.get(COMMENTS, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching comments:', error);
    }
}

export const postComment = async (commentData) => {
    try {
        await axios.post(COMMENTS, commentData, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
        });
    } catch (error) {
        console.error('Error adding comment:', error);
    }
}

export const removeComment = async (id) => {
    try {
        await axios.delete(COMMENTS, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
            data: {
                id: id,
            },
        });
    } catch (error) {
        console.error('Error removing comment:', error);
    }
}