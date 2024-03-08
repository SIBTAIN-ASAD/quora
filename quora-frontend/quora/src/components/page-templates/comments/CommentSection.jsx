// Comment.js
import React from 'react';

import { CommentList } from '../../organisms/index';

const CommentSection = () => {

    return (
        <div>
            <h3 className="text-xl mt-4 font-semibold">Comments</h3>
            <CommentList/>
        </div>
    );
};

export default CommentSection;
