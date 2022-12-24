import React from 'react';
import "./index.css";
import LandingBody from './body';
import LandingFooter from './footer';

export default function LandingPage() {
  return (
    <div className='landing-page'>
        <LandingBody/>
        <LandingFooter/>
    </div>
  )
}