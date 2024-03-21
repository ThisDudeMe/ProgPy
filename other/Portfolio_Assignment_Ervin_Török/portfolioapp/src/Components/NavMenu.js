import React from 'react';
import styles from '../Modules/NavMenu.module.css';

export const NavMenu = () => {
    return (
        <div className={styles.menuContainer}>
            <div>
                <div className={styles.menuText}>
                    Menu
                </div>

                <div className={styles.buttonsContainer}>
                    <button className={styles.menuButton} onClick={() => window.location.href="#aboutMeHyperLink"}>
                        About Me
                    </button>

                    <button className={styles.menuButton1}>
                        op2
                    </button>

                    <button className={styles.menuButton2}>
                        op3
                    </button>
                </div>

                <div className={styles.downloadButton}>
                    <a href="ph_cv.txt" download="mycv.txt">
                        <button>
                            Download My CV
                        </button>
                    </a>
                </div>
            </div>
        </div>
    );
};
