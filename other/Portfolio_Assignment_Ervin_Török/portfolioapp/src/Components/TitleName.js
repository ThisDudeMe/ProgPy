import React from 'react'
import styles from '../Modules/TitleName.module.css';

export const TitleName = () => {
    return (
        
        <div className={styles.titleContainer}> 
            
            <h1 className={styles.titleText}> Jon Doe </h1>
            <h2 className={styles.titleUnderText}> AI Developer </h2>

        </div>

    );
};