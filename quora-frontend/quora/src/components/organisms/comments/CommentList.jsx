// CommentList component to display the list of comments

import React, { useState, useEffect } from 'react';

import { fetchComments, removeComment } from '../../../services/commentAPIS';
import { Comment } from '../../molecules/index';

const CommentList = () => {
    const [comments, setComments] = useState([]);

    useEffect(() => {
        loadComments();
    }, []);

    const loadComments = async () => {
        const fetchedComments = await fetchComments();
        setComments(fetchedComments);
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
        <div className="mt-6 h-52 overflow-auto">
            {comments.map((comment, index) => (
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
