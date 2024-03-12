// Comment.js
import React from 'react';

import { CommentList } from '../../organisms/index';


const CommentSection = (props) => {
    const {comments, setComments } = props;

    return (
        <>
        <div>
            <h3 className="text-xl mt-4 font-semibold">Comments</h3>
            <CommentList 
                comments={comments}
                setComments={setComments}
            />
        </div>
        </>
    );
};

export default CommentSection;
