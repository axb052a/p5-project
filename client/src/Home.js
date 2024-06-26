// Home.js
import React, { useEffect, useState } from 'react';
import { Paper, Typography, Grid, CircularProgress } from '@mui/material';
import SearchBar from './SearchBar';
import { NavLink } from 'react-router-dom';
import MusicCard from './MusicCard';

function Home({ user }) {
  const [musicList, setMusicList] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch music data
    fetch('/api/music', { credentials: "include" })
      .then((response) => response.json())
      .then((data) => {
        setMusicList(data);
        setSearchResults(data);
        setLoading(false);
      })
      .catch((error) => console.error('Error fetching music:', error));
  }, []);

  const handleSearch = (searchTerm) => {
    if (!searchTerm || searchTerm.trim() === '') {
      setSearchResults(musicList);
    } else {
      setSearchResults(
        musicList.filter(
          (music) =>
            (music.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
              music.artist.toLowerCase().includes(searchTerm.toLowerCase()))
        )
      );
    }
  };

  const handleFavorite = (musicId, isFavorited) => {
  };

  return (
    <Grid
      container
      spacing={3}
      mt={3}
      style={{
        position: 'absolute',
        top: '64px', 
        left: 0,
        width: '100%',
        backgroundImage: 'url("https://wallpapers.com/images/hd/black-gradient-background-ov696eaxmtawst0g.jpg")',
        backgroundSize: 'cover',
        minHeight: 'calc(100vh - 64px)',
      }}
    >
      <Grid item xs={12}>
        <Paper
          elevation={3}
          style={{
            padding: '20px',
            margin: '20px',
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
          }}
        >
          <div>
            {user ? (
              <Typography variant="h5" gutterBottom>
                Welcome, {user.username} to Flatify!
              </Typography>
            ) : (
              <div>
                <img
                  src="https://t4.ftcdn.net/jpg/05/40/74/59/360_F_540745919_7LPqk3reCw26tdABJ1EsU6n4XsoI7f6U.jpg"
                  alt="Flatify Logo"
                  style={{
                    maxWidth: '600px',
                    display: 'block',
                    marginLeft: 'auto',
                    marginRight: 'auto',
                  }}
                />
                <Typography variant="h4" gutterBottom>
                  Welcome to Flatify!
                </Typography>
              </div>
            )}
          </div>
          {user ? (
            <>
              <Typography variant="body18" paragraph>
                Flatify is a platform to find and explore songs in multiple genres and playlists. Explore the Music Cards to see a song title associated with an artist, genre, and playlist.
                Listen to the songs in the {' '}
                <NavLink to="/musicplayer" style={{ textDecoration: 'none', color: "green", fontWeight: 'bold', fontSize: '1.0em' }}>
                  Music Player
                </NavLink>{' '} to determine which songs stand out to you. You could favorite your favorite songs.
              </Typography>
              <SearchBar onSearch={handleSearch} />
            </>
          ) : (
            <Typography variant="body18" paragraph>
              Welcome to Flatify! Flatify is a platform designed to help you find and explore songs, genres, and playlists. To get started, please{' '}
              <NavLink to="/login" style={{ textDecoration: 'none', color: "green", fontWeight: 'bold', fontSize: '1.0em' }}>
                Log In
              </NavLink>{' '}
              or{' '}
              <NavLink to="/signup" style={{ textDecoration: 'none', color: "green", fontWeight: 'bold', fontSize: '1.0em' }}>
                Sign Up
              </NavLink>
              . Our extensive database provides a comprehensive collection of music, making it accessible and tailored to your preferences.
              Whether you're a music enthusiast or someone curious about different genres, Flatify offers a personalized listening experience.
              Unlock the world of music and expand your playlist. Join us on this musical journey as we make discovering new songs exciting.
              Start your exploration today! Visit
              {' '}<NavLink to="/about" style={{ textDecoration: 'none', color: "green", fontWeight: 'bold', fontSize: '1.0em' }}>
                About
              </NavLink>{' '}
              to learn more about the app and its functionality. Read my 
              {' '}<NavLink to="/biography" style={{ textDecoration: 'none', color: "green", fontWeight: 'bold', fontSize: '1.0em' }}>
                Biography
              </NavLink>{' '}
              to learn and get to know me on a personal level as a software engineer. 
            </Typography>
          )}
        </Paper>
      </Grid>
      {user && (
        <Grid item xs={12}>
          {loading ? (
            <CircularProgress />
          ) : (
            <Grid container spacing={3}>
              {Array.isArray(searchResults) ? (
                searchResults.map((music) => (
                  <Grid item key={music.id} xs={12} sm={6} md={4} lg={3}>
                    <MusicCard
                      id={music.id}
                      title={music.title}
                      artist={music.artist}
                      image={music.image}
                      genre={music.genre}
                      playlist={music.playlist}
                      onFavorite={handleFavorite}
                    />
                  </Grid>
                ))
              ) : (
                <p>Error</p>
              )}
            </Grid>
          )}
        </Grid>
      )}
    </Grid>
  );
}

export default Home;
