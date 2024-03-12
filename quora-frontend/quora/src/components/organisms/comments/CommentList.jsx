import React from 'react';

import { removeComment } from '../../../services/commentAPIS';
import { Comment } from '../../molecules/index';

const CommentList = (props) => {
    
    const {comments, setComments } = props;

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
            {(comments.length !== 0) && comments.map((comment, index) => (
                <Comment
                    key={index}
                    comment={comment}
                    onDelete={handleDeleteComment}
                />
            ))}
        </div>
    );
};

export default CommentList;
