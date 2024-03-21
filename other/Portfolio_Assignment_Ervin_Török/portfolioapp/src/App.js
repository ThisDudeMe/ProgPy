import React from "react";
import styles from './App.css'
import { TitleName } from "./Components/TitleName";
import { NavMenu } from "./Components/NavMenu";
import { AboutMe } from "./Components/AboutMe";
import { PaddingBlock } from "./Components/PaddingBlock";
import { SkillsEducation } from "./Components/SkillsEducation";
import { BestWork } from "./Components/BestWork";
import { ReferencesContact } from "./Components/ReferencesContact";
import { Footer } from "./Components/Footer";

function App() {
  return (
    <div className={styles.siteBackground}>

      <PaddingBlock />
      <TitleName />
      <PaddingBlock />
      <NavMenu />
      <PaddingBlock />
      <AboutMe />
      <PaddingBlock />
      <SkillsEducation />
      <PaddingBlock />
      <BestWork />
      <PaddingBlock />
      <ReferencesContact />
      <PaddingBlock />
      <Footer />
      <PaddingBlock />

    </div>
  );
};

export default App;
