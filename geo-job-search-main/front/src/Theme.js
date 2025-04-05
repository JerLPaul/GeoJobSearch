import styled, { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  body {
    background-color: #272730;
    color: #fffffe;
    font-family: sans-serif;
    margin: 0;
    padding: 0;
  }

  a {
    color: #7f5af0;
    text-decoration: none;
  }

  a:hover {
    color: #2cb67d;
  }

  .highlight {
    background-color: #7f5af0;
    color: #fffffe;
  }

  .secondary {
    color: #72757e;
  }

  .tertiary {
    color: #2cb67d;
  }
`;

export const Container = styled.div`
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
`;

export const Heading = styled.h1`
  font-size: 2em;
  margin-bottom: 10px;
`;

export const Text = styled.p`
  font-size: 1em;
  line-height: 1.5;
`;

export default GlobalStyles;
