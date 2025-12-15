import { useState } from "react";
import { Button } from "@components";
import logo from "@/assets/logo.svg";
export const NavBar = () => {
  const [hovered, setHovered] = useState<boolean>(false);

  const LogoTextClasses = "font-[800] text-[24px]";
  const BaseTextClasses = "font-[700] text-[20px] cursor-pointer";

  return (
    <nav className="flex items-center justify-between bg-[#FBF6F699] bg-opacity-60 rounded-b-[30px] h-[110px] ">
      <div className="flex items-center gap-[19px] pl-[30px] pt-[9.44px] pb-[24.86px]">
        <img src={logo} alt="Logo" className="w-[59.67px] h-[75.7px]" />
        <div className="pt-4">
          <span className={`${LogoTextClasses} `}>DZ </span>
          <span className={`${LogoTextClasses} text-[#DCA934]`}>Stagiaire</span>
        </div>
      </div>

      <div className="flex gap-[60px]">
        <span
          className={`${BaseTextClasses} ${
            hovered ? "text-black" : "text-[#DCA934]"
          }`}
        >
          Service
        </span>
        <span
          className={`${BaseTextClasses} ${
            hovered ? " text-[#DCA934] hover:-translate-x-2 transition-all duration-100 slow" : "text-black"
          }`}
          onMouseEnter={()=> setHovered(true)}
          onMouseLeave={()=> setHovered(false)}
        >
          À propos
        </span>
      </div>

      <div className="flex gap-[20px] pr-[109px]">
        <Button variant="mo9a3ar" size="small" disabled={false}>
          Log in
        </Button>
        <Button variant="moba6an" size="small" disabled={false}>
          Log in
        </Button>
      </div>
    </nav>
  );
};
