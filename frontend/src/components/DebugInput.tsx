import React from "react";
import '../styles/component-styles/DebugInput.scss';

const  DebugInput = () => {
    return (

      <form className="debug-wrapper">
        <label>
          Message:
          <br/>
          <textarea name="message" />
        </label>
        <br/>
        <input type="submit" value="Submit" />
      </form>

    );
  }

export default DebugInput;