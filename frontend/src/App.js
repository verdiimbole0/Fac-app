import React from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { StoreProvider } from "@/context/StoreContext";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import AnnouncementBar from "@/components/layout/AnnouncementBar";
import CartDrawer from "@/components/cart/CartDrawer";
import SearchOverlay from "@/components/search/SearchOverlay";
import Home from "@/pages/Home";
import Category from "@/pages/Category";
import ProductDetail from "@/pages/ProductDetail";
import Wishlist from "@/pages/Wishlist";
import Checkout from "@/pages/Checkout";
import { Toaster } from "@/components/ui/sonner";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <StoreProvider>
          <AnnouncementBar />
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/c/:slug" element={<Category />} />
            <Route path="/product/:slug" element={<ProductDetail />} />
            <Route path="/wishlist" element={<Wishlist />} />
            <Route path="/checkout" element={<Checkout />} />
          </Routes>
          <Footer />
          <CartDrawer />
          <SearchOverlay />
          <Toaster
            position="bottom-center"
            toastOptions={{
              style: {
                background: "#1a1a1a",
                color: "#fafaf7",
                border: "1px solid #333",
                borderRadius: 0,
                fontFamily: "Manrope, sans-serif",
              },
            }}
          />
        </StoreProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
