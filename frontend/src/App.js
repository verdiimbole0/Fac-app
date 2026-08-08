import React from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { StoreProvider } from "@/context/StoreContext";
import { AuthProvider } from "@/context/AuthContext";
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
import PaymentResult from "@/pages/PaymentResult";
import AuthCallback from "@/pages/AuthCallback";
import AdminLogin from "@/pages/admin/AdminLogin";
import AdminLayout from "@/pages/admin/AdminLayout";
import AdminDashboard from "@/pages/admin/AdminDashboard";
import AdminProducts from "@/pages/admin/AdminProducts";
import AdminProductEdit from "@/pages/admin/AdminProductEdit";
import AdminOrders from "@/pages/admin/AdminOrders";
import AdminPromos from "@/pages/admin/AdminPromos";
import { Toaster } from "@/components/ui/sonner";

function Shell({ children }) {
  const location = useLocation();
  const isAdmin = location.pathname.startsWith("/admin");
  // Detect Emergent auth callback fragment at ANY route - defer to AuthCallback
  if (location.hash?.includes("session_id=")) {
    return <AuthCallback />;
  }
  if (isAdmin) return children;
  return (
    <>
      <AnnouncementBar />
      <Header />
      {children}
      <Footer />
      <CartDrawer />
      <SearchOverlay />
    </>
  );
}

function AppRoutes() {
  return (
    <Shell>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/c/:slug" element={<Category />} />
        <Route path="/product/:slug" element={<ProductDetail />} />
        <Route path="/wishlist" element={<Wishlist />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/payment/result" element={<PaymentResult />} />
        <Route path="/admin/auth-callback" element={<AuthCallback />} />
        <Route path="/admin/login" element={<AdminLogin />} />
        <Route path="/admin" element={<AdminLayout />}>
          <Route index element={<AdminDashboard />} />
          <Route path="products" element={<AdminProducts />} />
          <Route path="products/new" element={<AdminProductEdit />} />
          <Route path="products/:slug" element={<AdminProductEdit />} />
          <Route path="orders" element={<AdminOrders />} />
          <Route path="promos" element={<AdminPromos />} />
        </Route>
      </Routes>
    </Shell>
  );
}

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AuthProvider>
          <StoreProvider>
            <AppRoutes />
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
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
