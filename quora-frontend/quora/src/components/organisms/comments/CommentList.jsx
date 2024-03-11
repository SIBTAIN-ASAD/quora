import React, { useState, useEffect } from 'react';

import { fetchComments, removeComment } from '../../../services/commentAPIS';
import { Comment } from '../../molecules/index';
import { LoadingOverlay } from '../../organisms/index'; // Assuming you have a LoadingOverlay component

const CommentList = () => {
    const [comments, setComments] = useState([]);
    const [isLoading, setLoading] = useState(true); // State to manage loading

    useEffect(() => {
        loadComments();
    }, []);

    const loadComments = async () => {
        try {
            const fetchedComments = await fetchComments();
            setComments(fetchedComments.user_rating_comment);
        } catch (error) {
            console.error('Error fetching comments:', error.message);
        } finally {
            setLoading(false); // Set loading to false after fetching
        }
    };


    const handleDeleteComment = async (commentId) => {
        try {
            await removeComment(commentId);
            setComments(comments.filter(comment => comment.id !== commentId));
        } catch (error) {
            console.error('Error removing comment:', error.message);
        }
    };

    return (
        <div className="mt-6 h-52 overflow-auto relative">
            {isLoading && <LoadingOverlay />} {/* Show loading overlay when loading is true */}
            {!isLoading && (comments.length !== 0) && comments.map((comment, index) => (
                <Comment
                    key={index}
                    comment={comment}
                    onDelete={() => handleDeleteComment}
                />
            ))}
        </div>
    );
};

export default CommentList;
