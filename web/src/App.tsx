import Navbar from "./componends/Navbar.tsx";
import Home from "./componends/Home.tsx";
import Blends from "./componends/Blends.tsx";
import {RouterProvider, createHashRouter} from "react-router-dom";

const router = createHashRouter([
    {
        path: '/',
        element: <Home />,
    },
    {
        path: '/blends',
        element: <Blends />,
    }
]);
function App() {
  return (
      <>
          <Navbar />
          <RouterProvider router={router}/>
      </>
  )
}
export default App;