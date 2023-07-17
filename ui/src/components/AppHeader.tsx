import { useEffect, useState } from "react";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";

import { AccountApi } from "../api/AccountApi";
import { User } from "../gensrc/api/data-contracts";

export default function AppHeader(props) {
  const [user, setUser] = useState<User | null>(null);
  useEffect(() => {
    AccountApi.getProfile().then((resp) => {
      setUser(resp);
    });
  }, []);
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <a href="/">Hangboard</a>
          </Typography>
          {user === null ? (
            <Button color="inherit" href="/login">
              Login
            </Button>
          ) : (
            <div>{user.username}</div>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
}
