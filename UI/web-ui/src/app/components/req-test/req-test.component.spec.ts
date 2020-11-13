import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReqTestComponent } from './req-test.component';

describe('ReqTestComponent', () => {
  let component: ReqTestComponent;
  let fixture: ComponentFixture<ReqTestComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReqTestComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReqTestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
