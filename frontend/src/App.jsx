import React from 'react';
import { Container } from "@material-ui/core";
import Layout from "./containers/Layout";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  container: {
    marginTop: '5rem',
  },
}));

function App() {
  const classes = useStyles();

  return (
    <Container maxWidth="lg" className={classes.container}>
      <Layout />
    </Container>
  );
}

export default App;
