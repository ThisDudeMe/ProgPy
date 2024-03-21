import React from 'react';
import styles from '../Modules/AboutMe.module.css';

export const AboutMe = () => {
  return (
    <div id='aboutMeHyperLink' className={styles.aboutMeContainer}>
      <div className={styles.aboutMeTitle}>
          About Me
      </div>

      <div className={styles.aboutMeContent}>
          <div className={styles.aboutMeImage}>
            <img src="/PH_portrait.jpg" alt="portrait image" />
          </div>

          <div className={styles.aboutMeText}>                
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Magni sapiente soluta numquam sunt voluptate cumque odio sit, 
            quis amet hic voluptatem animi perferendis iusto consectetur alias? 
            Tenetur tempora illum dolores?
          </div>
      </div>
    </div>
  );
};
