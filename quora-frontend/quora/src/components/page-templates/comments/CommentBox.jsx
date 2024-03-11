// File contains comments section and form

import React, { useState } from 'react';

import { CommentForm } from '../../organisms/index';
import { CommentSection } from './CommentSection';

const CommentBox = () => {

    // state to keep track whether there is need to refresh the comments or not
    const [refreshComments, setRefreshComments] = useState(false);

    return (
        <div>
            <CommentForm setRefreshComments={setRefreshComments} />
            <CommentSection refreshComments={refreshComments} />
        </div>
    );
}

export default CommentBox;