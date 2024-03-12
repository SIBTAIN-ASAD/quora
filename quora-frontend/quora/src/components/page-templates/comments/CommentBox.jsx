// File contains comments section and form

import React, { useState, useEffect } from 'react';


import { CommentForm } from '../../organisms/index';
import CommentSection from './CommentSection';
import { fetchComments } from '../../../services/commentAPIS';

const CommentBox = () => {

    const [comments, setComments] = useState([]);

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
        }
    };


    return (
        <>
            <div>
                <CommentForm
                    setComments={setComments} />
                <CommentSection
                    comments={comments}
                    setComments={setComments}
                />
            </div>
        </>
    );
}

export default CommentBox;
