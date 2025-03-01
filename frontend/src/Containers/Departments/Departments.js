import React from "react";
import DepartmentCard from "../../Components/DepartmentCard/DepartmentCard";
import {useSelector} from 'react-redux';

const Departments = () => {
  const dataArray = useSelector((state) => state.departments);
  if (dataArray) {
    console.log(dataArray);
  }
  
  return (
    <div>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 h-full">
        <DepartmentCard alignment={1}/>
        <DepartmentCard alignment={2}/>
        <DepartmentCard alignment={3}/>
        <DepartmentCard alignment={1}/>
        <DepartmentCard alignment={2}/>
        <DepartmentCard alignment={3}/>
      </div>
    </div>
  );
};

export default Departments;
